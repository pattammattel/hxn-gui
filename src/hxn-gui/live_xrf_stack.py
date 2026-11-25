"""Live XRF stack viewer for angle-series scans (tomography now, diffraction later).

The plan rewrites its angle log (save_log_to/<scan_label>_startID<first_sid>.csv) after each angle,
filling in the scan_id of that angle's 2D map. The viewer polls the log, loads new scans in a background thread,
saves each as <log folder>/<prefix>_live_images/scan_<sid>.npz (stack, elems, angle), and displays from those
files; scans already saved are not fetched again. and shows four user-selected elements, sorted by angle,
with one shared slider.
"""
import csv
import json
import glob
import os
import time

import numpy as np
import pyqtgraph as pg
from qtpy import QtCore, QtWidgets
from qtpy.QtCore import QThread, Qt, Signal

N_VIEWS = 4
POLL_MS = 10 * 60 * 1000


def get_all_xrf_roi_data(hdr, channels=(1, 2, 3)):
    """Return (stack[n_elem, ny, nx], sorted element names) summed over the XRF channels."""
    keys = list(hdr.table().keys())
    elem_list = sorted(k.replace("Det1_", "") for k in keys if k.startswith("Det1_"))
    start = hdr.start
    try:
        nx, ny = start["dimensions"] if "dimensions" in start else start["shape"]
        shape = (ny, nx)  # fly2d data is row-major in y, as in 53-viewer2d.py
    except Exception as exc:
        print(f"[DATA ERROR] cannot get scan dimensions, defaulting to (1, n_events). Error: {exc}")
        shape = (1, len(hdr.table()))
    images = []
    for elem in elem_list:
        spectrum = np.sum([np.asarray(list(hdr.data(f"Det{ch}_{elem}")), dtype=np.float32).squeeze()
                           for ch in channels], axis=0)
        images.append(spectrum.reshape(shape))
    return np.stack(images, axis=0), elem_list


def read_angle_log(path):
    """Return [(scan_id, angle)] from the plan's angle-log CSV; rows not yet scanned are skipped."""
    entries, seen = [], set()
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            try:
                sid, angle = int(float(row["scan_id"])), float(row["angle"])
            except (KeyError, TypeError, ValueError):
                continue  # empty scan_id: angle not measured yet
            if sid not in seen:
                seen.add(sid)
                entries.append((sid, angle))
    return entries


def newest_log(pattern, newer_than=None):
    """Newest file matching pattern, optionally modified at or after newer_than (epoch s)."""
    paths = [p for p in glob.glob(pattern) if newer_than is None or os.path.getmtime(p) >= newer_than]
    return max(paths, key=os.path.getmtime) if paths else None


def get_scan_extent(hdr):
    """Scan area from the start document: dict x0, x1, y0, y1 (motor units) and axis labels, or None."""
    start = hdr.start
    try:
        (x0, x1), (y0, y1) = start["scan_range"]
    except Exception:
        return None
    motors = list(start.get("motors", []))
    xlabel = motors[0] if len(motors) > 0 else "x"
    ylabel = motors[1] if len(motors) > 1 else "y"
    return {"x0": float(x0), "x1": float(x1), "y0": float(y0), "y1": float(y1),
            "xlabel": str(xlabel), "ylabel": str(ylabel)}


IMAGE_KEYS = ("merlin1", "merlin2", "eiger2_image", "eiger1_image", "eiger1", "eiger2")


def find_image_key(hdr):
    """Name of the area-detector image stream in a scan (preferring the HXN detectors in IMAGE_KEYS)."""
    found = []
    for desc in hdr.descriptors:
        for key, info in desc.get("data_keys", {}).items():
            if len(info.get("shape") or []) >= 2:
                found.append(key)
    for key in IMAGE_KEYS:
        if key in found:
            return key
    if found:
        return found[0]
    raise KeyError("no area-detector images in this scan")


def get_diff_sum_map(hdr, det=None, norm="sclr1_ch4", threshold=(0, 1e6)):
    """Diffraction intensity map (ny, nx): mean of each detector frame / monitor, as plot_img_sum in
    53-viewer2d.py (pixels outside threshold set to 0). Frames are reduced one at a time, so memory stays small.

    Returns (image, det).
    """
    det = det or find_image_key(hdr)
    sums = []
    for frame in hdr.data(det):
        arr = np.asarray(frame, dtype=np.float32)
        arr = np.where((arr < threshold[0]) | (arr > threshold[1]), 0, arr)
        if arr.ndim > 2:  # several frames per event: one value per frame
            sums.extend(arr.reshape(-1, arr.shape[-2], arr.shape[-1]).mean(axis=(1, 2)))
        else:
            sums.append(arr.mean())
    tot = np.asarray(sums, dtype=np.float32)
    if norm:
        mon = np.asarray(list(hdr.data(norm)), dtype=np.float32).ravel()[:tot.size]
        with np.errstate(divide="ignore", invalid="ignore"):
            tot = tot[:mon.size] / np.where(mon == 0, np.nan, mon)
    start = hdr.start
    try:
        nx, ny = start["dimensions"] if "dimensions" in start else start["shape"]
    except Exception:
        nx, ny = tot.size, 1
    frame = np.zeros(nx * ny, dtype=np.float32)  # unfinished scans: pad like plot_img_sum
    frame[:min(tot.size, frame.size)] = tot[:frame.size]
    return frame.reshape(ny, nx), det


def save_stack(path, stack, elems, sid, angle, extent=None):
    """Write one scan's stack atomically, so a reader never sees a half-written file."""
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        np.savez(f, stack=np.asarray(stack, dtype=np.float32), elems=np.array(elems), sid=sid, angle=angle,
                 extent=json.dumps(extent))
    os.replace(tmp, path)


def load_stack(path):
    """Return (stack, elems, extent); extent is None for files saved without one."""
    with np.load(path) as data:
        extent = json.loads(str(data["extent"])) if "extent" in data.files else None
        return data["stack"], [str(e) for e in data["elems"]], extent


def pinned_path(save_dir, sid, label):
    return os.path.join(save_dir, f"scan_{sid}_{label}.npz")


class StackLoader(QThread):
    """Off the GUI thread: reuse save_dir/scan_<sid>.npz if present, else fetch(sid) and save it.

    With pinned=(label, fetch), after all XRF stacks it computes the slow pinned map for each scan
    (pinned fetch(sid) -> (image, extent)) into scan_<sid>_<label>.npz.
    """
    loaded = Signal(int, float, str, object)
    pinned_loaded = Signal(int, str)
    failed = Signal(int, str)
    progress = Signal(str)

    def __init__(self, fetch, entries, save_dir, pinned=None, parent=None):
        super().__init__(parent)
        self.fetch, self.entries, self.save_dir, self.pinned = fetch, entries, save_dir, pinned

    def run(self):
        self._load_xrf()
        if self.pinned:
            self._load_pinned()

    def _load_pinned(self):
        label, fetch = self.pinned
        for n, (sid, angle) in enumerate(self.entries, 1):
            if self.isInterruptionRequested():
                return
            path = pinned_path(self.save_dir, sid, label)
            try:
                if not os.path.isfile(path):
                    self.progress.emit(f"Computing {label} for scan {sid} ({n}/{len(self.entries)}); this can take a while...")
                    t0 = time.monotonic()
                    image, extent = fetch(sid)
                    os.makedirs(self.save_dir, exist_ok=True)
                    save_stack(path, np.asarray(image)[None], [label], sid, angle, extent)
                    print(f"[LIVE STACK] scan {sid} {label}: shape {np.shape(image)} in "
                          f"{time.monotonic() - t0:.0f} s -> {path}")
                self.pinned_loaded.emit(sid, path)
            except Exception as exc:
                self.failed.emit(sid, f"{label}: {type(exc).__name__}: {exc}")

    def _load_xrf(self):
        for sid, angle in self.entries:
            if self.isInterruptionRequested():
                return
            path = os.path.join(self.save_dir, f"scan_{sid}.npz")
            try:
                if os.path.isfile(path):
                    _, elems, _ = load_stack(path)
                else:
                    result = self.fetch(sid)  # (stack, elems) or (stack, elems, extent)
                    stack, elems = result[0], list(result[1])
                    extent = result[2] if len(result) > 2 else None
                    os.makedirs(self.save_dir, exist_ok=True)
                    save_stack(path, stack, elems, sid, angle, extent)
                    finite = np.isfinite(stack)
                    print(f"[LIVE STACK] scan {sid} @ {angle:.2f} deg: shape {np.shape(stack)}, "
                          f"{len(elems)} elements, {np.size(stack) - finite.sum()} non-finite values -> {path}")
                self.loaded.emit(sid, angle, path, elems)
            except Exception as exc:
                self.failed.emit(sid, f"{type(exc).__name__}: {exc}")


class XrfStackViewer(QtWidgets.QWidget):
    """Four image views with element pickers, one angle slider, Update Now and Load buttons.

    Follow a scan with follow_log(pattern, newer_than) (the CSV name is only known once the plan
    starts), or open a specific angle-log CSV with Load Angle Log.

    prefix names the child widgets (e.g. "tomo" -> pb_tomo_live_update) so tooltips.json can target them.
    fetch(sid) returns (stack, elems); default_elems() returns preferred element names.
    """

    def __init__(self, prefix, fetch, default_elems=lambda: [], pinned=None, parent=None):
        """pinned=(label, fetch): view 1 always shows that slow map (e.g. diff_sum) instead of an element."""
        super().__init__(parent)
        self.prefix, self.fetch, self.default_elems, self.pinned = prefix, fetch, default_elems, pinned
        self.log_path = None
        self.log_pattern, self.log_newer_than = None, None
        self.frames = []  # dicts: sid, angle, path (.npz on disk), elems; kept sorted by angle
        self._cache = (None, None)  # (path, stack) of the frame on screen
        self.failed = {}
        self.loader = None
        self._build()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_now)
        self.timer.start(POLL_MS)

    def _name(self, w, suffix):
        w.setObjectName(f"{suffix.split('_')[0]}_{self.prefix}_live_{suffix.split('_', 1)[1]}")
        return w

    def _build(self):
        grid = QtWidgets.QGridLayout(self)
        grid.setContentsMargins(0, 0, 0, 0)
        self.views, self.combos = [], []
        for i in range(N_VIEWS):
            view = pg.ImageView(view=pg.PlotItem())
            view.setObjectName(f"iv_{self.prefix}_live_{i + 1}")
            view.ui.roiBtn.hide()
            view.ui.menuBtn.hide()
            view.setColorMap(pg.colormap.get("viridis"))
            view.getView().setAspectLocked(True)
            view.getView().invertY(False)
            view.setMinimumSize(220, 220)
            combo = self._name(QtWidgets.QComboBox(), f"cb_elem_{i + 1}")
            if i == 0 and self.pinned:
                combo.addItem(self.pinned[0])
                combo.setEnabled(False)
            combo.currentTextChanged.connect(lambda _t, k=i: self._show_view(k))
            grid.addWidget(view, 0, i)
            grid.addWidget(combo, 1, i)
            self.views.append(view)
            self.combos.append(combo)

        self.slider = self._name(QtWidgets.QSlider(Qt.Horizontal), "sl_angle")
        self.slider.setEnabled(False)
        self.slider.valueChanged.connect(lambda _v: self._show_all())
        self.label_frame = self._name(QtWidgets.QLabel("No data"), "label_frame")
        self.label_frame.setMinimumWidth(260)
        bar = QtWidgets.QHBoxLayout()
        bar.addWidget(self.slider, 1)
        bar.addWidget(self.label_frame)
        grid.addLayout(bar, 2, 0, 1, N_VIEWS)

        self.pb_update = self._name(QtWidgets.QPushButton("Update Now"), "pb_update")
        self.pb_update.clicked.connect(self.update_now)
        self.pb_load = self._name(QtWidgets.QPushButton("Load Angle Log..."), "pb_load")
        self.pb_load.clicked.connect(self._choose_log)
        self.label_status = self._name(QtWidgets.QLabel("No angle log"), "label_status")
        self.label_status.setTextInteractionFlags(Qt.TextSelectableByMouse)
        row = QtWidgets.QHBoxLayout()
        row.addWidget(self.pb_update)
        row.addWidget(self.pb_load)
        row.addWidget(self.label_status, 1)
        grid.addLayout(row, 3, 0, 1, N_VIEWS)

    # ---- data ----
    def follow_log(self, pattern, newer_than=None):
        """Follow the newest angle log matching pattern written at/after newer_than (scan just started)."""
        self.log_pattern, self.log_newer_than = pattern, newer_than
        self._reset(None)

    def set_log(self, path):
        """Show a specific angle-log CSV."""
        self.log_pattern = None
        self._reset(path)

    def _reset(self, path):
        self.stop()
        self.log_path = path
        self.frames, self.failed = [], {}
        self._cache = (None, None)
        for view in self.views:
            view.clear()
            view._last_shape = None
        self._refresh_slider()
        self.update_now()

    def _choose_log(self):
        start = os.path.dirname(self.log_path or self.log_pattern or "")
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Angle Log", start,
                                                        "Angle logs (*.csv);;All files (*)")
        if path:
            self.set_log(path)

    def update_now(self):
        if self.log_pattern is not None:
            found = newest_log(self.log_pattern, self.log_newer_than)
            if found is None:
                self.label_status.setText(f"Waiting for the angle log in {os.path.dirname(self.log_pattern)} "
                                          "(written after the first angle finishes).")
                return
            if found != self.log_path:
                self._reset(found)  # first log, or a newer run of the same label
                return
        if self.log_path is None:
            self.label_status.setText("No angle log. Start a scan, or load an angle-log CSV.")
            return
        if self.loader is not None and self.loader.isRunning():
            self.label_status.setText("Still loading earlier scans; try again when it finishes.")
            return
        if not os.path.isfile(self.log_path):
            self.label_status.setText(f"Angle log not found: {self.log_path}")
            return
        complete = {f["sid"] for f in self.frames if not self.pinned or f.get("pinned")}
        new = [e for e in read_angle_log(self.log_path) if e[0] not in complete]
        if not new:
            self._status("Up to date.")
            return
        self.label_status.setText(f"Loading {len(new)} new scan(s)...")
        self.pb_update.setEnabled(False)
        self.loader = StackLoader(self.fetch, new, self.save_dir(), self.pinned, self)
        self.loader.loaded.connect(self._add_frame)
        self.loader.pinned_loaded.connect(self._add_pinned)
        self.loader.progress.connect(self.label_status.setText)
        self.loader.failed.connect(self._failed)
        self.loader.finished.connect(self._load_finished)
        self.loader.start()

    def save_dir(self):
        """<log folder>/<prefix>_live_images, e.g. save_log_to/tomo_live_images."""
        return os.path.join(os.path.dirname(os.path.abspath(self.log_path)), f"{self.prefix}_live_images")

    def _add_frame(self, sid, angle, path, elems):
        self.failed.pop(sid, None)
        if any(f["sid"] == sid for f in self.frames):
            return
        current = self._current_frame()
        self.frames.append({"sid": sid, "angle": angle, "path": path, "elems": elems})
        self.frames.sort(key=lambda f: f["angle"])
        self._fill_combos(elems)
        self._refresh_slider(keep=current["sid"] if current else sid)

    def _add_pinned(self, sid, path):
        frame = next((f for f in self.frames if f["sid"] == sid), None)
        if frame is None:
            return
        frame["pinned"] = path
        if frame is self._current_frame():
            self._show_view(0)

    def _failed(self, sid, msg):
        self.failed[sid] = msg
        print(f"[LIVE STACK] scan {sid} not loaded: {msg}")

    def _load_finished(self):
        self.pb_update.setEnabled(True)
        self._status("Updated.")

    def _status(self, what):
        msg = (f"{what} {len(self.frames)} angle(s) from {os.path.basename(self.log_path)}; "
               f"images in {self.save_dir()}.")
        if self.failed:
            msg += f" Failed (retried on next update): {sorted(self.failed)}"
        self.label_status.setText(msg)

    def stop(self):
        if self.loader is not None and self.loader.isRunning():
            self.loader.requestInterruption()
            self.loader.wait(5000)

    # ---- display ----
    def _fill_combos(self, elems):
        if [self.combos[0].itemText(i) for i in range(self.combos[0].count())] == elems:
            return
        first = 1 if self.pinned else 0
        preferred = [e for e in self.default_elems() if e in elems]
        picks = (preferred + [e for e in elems if e not in preferred])[:N_VIEWS - first]
        for i, combo in enumerate(self.combos[first:]):
            keep = combo.currentText()
            with QtCore.QSignalBlocker(combo):
                combo.clear()
                combo.addItems(elems)
                combo.setCurrentText(keep if keep in elems else (picks[i] if i < len(picks) else elems[0]))

    def _refresh_slider(self, keep=None):
        n = len(self.frames)
        with QtCore.QSignalBlocker(self.slider):
            self.slider.setEnabled(n > 1)
            self.slider.setRange(0, max(n - 1, 0))
            if keep is not None:
                idx = next((i for i, f in enumerate(self.frames) if f["sid"] == keep), n - 1)
                self.slider.setValue(idx)
        self._show_all()

    def _current_frame(self):
        if not self.frames:
            return None
        return self.frames[min(self.slider.value(), len(self.frames) - 1)]

    def _frame_stack(self, frame):
        if self._cache[0] != frame["path"]:
            stack, _, extent = load_stack(frame["path"])
            self._cache = (frame["path"], (stack, extent))
        return self._cache[1]

    def _show_all(self):
        frame = self._current_frame()
        if frame is None:
            self.label_frame.setText("No data")
            return
        self.label_frame.setText(f"{frame['angle']:.2f}\u00b0  scan {frame['sid']}  "
                                 f"({self.slider.value() + 1}/{len(self.frames)})")
        for i in range(N_VIEWS):
            self._show_view(i)

    def _show_view(self, i):
        frame = self._current_frame()
        elem = self.combos[i].currentText()
        if frame is None:
            self.views[i].clear()
            return
        try:
            if i == 0 and self.pinned:
                if not frame.get("pinned"):
                    self.views[i].clear()
                    self.views[i].setToolTip(f"{elem} for scan {frame['sid']} is not computed yet.")
                    return
                stack, _, extent = load_stack(frame["pinned"])
                image = stack[0]
            elif elem in frame["elems"]:
                stack, extent = self._frame_stack(frame)
                image = stack[frame["elems"].index(elem)]
            else:
                self.views[i].clear()
                return
        except Exception as exc:
            self.label_status.setText(f"Cannot read data for scan {frame['sid']}: {exc}")
            self.views[i].clear()
            return
        image = np.asarray(image, dtype=np.float32)
        view = self.views[i]
        # NaN/inf would make pyqtgraph's auto contrast NaN and draw nothing; level from finite pixels.
        finite = image[np.isfinite(image)]
        lo, hi = (float(finite.min()), float(finite.max())) if finite.size else (0.0, 1.0)
        if hi <= lo:
            hi = lo + 1.0
        image = np.nan_to_num(image, nan=lo, posinf=hi, neginf=lo)
        self.views[i].setToolTip(f"{elem}: {image.shape[1]} x {image.shape[0]} px, min {lo:.3g}, max {hi:.3g}")
        ny, nx = image.shape
        if extent:
            pos = (extent["x0"], extent["y0"])
            scale = ((extent["x1"] - extent["x0"]) / nx, (extent["y1"] - extent["y0"]) / ny)
            labels = (f"{extent['xlabel']} (\u00b5m)", f"{extent['ylabel']} (\u00b5m)")
        else:
            pos, scale, labels = (0, 0), (1, 1), ("x (pixel)", "y (pixel)")
        plot = view.getView()
        plot.setLabel("bottom", labels[0])
        plot.setLabel("left", labels[1])
        # Fit the view only when the image area changes, so zoom survives slider moves.
        key = (image.shape, pos, scale)
        refit = getattr(view, "_last_shape", None) != key
        view._last_shape = key
        # pyqtgraph images are (x, y); transpose the (row=y, col=x) array.
        view.setImage(image.T, autoRange=refit, autoLevels=False, levels=(lo, hi), pos=pos, scale=scale)
