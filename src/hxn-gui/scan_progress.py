"""Live progress of an angle-series scan (tomo / diff), read from the plan's angle-log CSV.

The plan writes every planned angle as a row at scan start (TimeStamp = start time, scan_id empty) and fills
in scan_id and TimeStamp as each angle finishes, rewriting the CSV each time.
"""
import csv
import json
import os
import time
from datetime import datetime, timedelta

from qtpy import QtCore, QtWidgets
from qtpy.QtCore import Signal

from live_xrf_stack import newest_log

# Poll at 1/POLL_FRACTION of the measured time per angle, within these bounds; FIRST_POLL_MS until it is known.
POLL_FRACTION = 5
MIN_POLL_MS, MAX_POLL_MS, FIRST_POLL_MS = 2 * 1000, 30 * 1000, 5 * 1000


def read_progress(log_path, skip_angles=()):
    """Summarize the angle log. skip_angles: angles the plan skips (remove_angles), not counted as remaining.

    Returns dict(done, total, current, start, last_done, per_angle, finish) or raises on unreadable files.
    """
    done, todo, stamps = [], [], []
    with open(log_path, newline="") as f:
        for row in csv.DictReader(f):
            try:
                angle = float(row["angle"])
            except (KeyError, TypeError, ValueError):
                continue
            try:
                stamp = datetime.fromisoformat(row.get("TimeStamp", "").strip())
                stamps.append(stamp)
            except ValueError:
                stamp = None
            if (row.get("scan_id") or "").strip():
                done.append((angle, stamp))
            elif not any(abs(angle - a) < 1e-3 for a in skip_angles):
                todo.append(angle)
    start = min(stamps) if stamps else None
    finished = [s for _a, s in done if s is not None]
    last_done = max(finished) if finished else None
    per_angle = (last_done - start) / len(done) if done and start and last_done and last_done > start else None
    finish = last_done + per_angle * len(todo) if per_angle and todo else None
    return {"done": len(done), "total": len(done) + len(todo), "current": todo[0] if todo else None,
            "start": start, "last_done": last_done, "per_angle": per_angle, "finish": finish}


def _fmt(td):
    minutes = int(td.total_seconds() // 60)
    return f"{minutes // 60} h {minutes % 60:02d} min" if minutes >= 60 else f"{minutes} min"


class ScanProgress(QtWidgets.QWidget):
    """Progress bar and text for the scan started from a tab; prefix names widgets for tooltips.json."""
    finished = Signal()  # emitted once per followed scan, when the log shows every angle done

    def __init__(self, prefix, parent=None):
        super().__init__(parent)
        self.log_pattern = self.newer_than = self.json_path = self.log_path = None
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.bar = QtWidgets.QProgressBar()
        self.bar.setObjectName(f"pbar_{prefix}_progress")
        self.bar.setFormat("%v / %m angles")
        self.bar.setRange(0, 1)
        self.bar.setValue(0)
        self.label = QtWidgets.QLabel("No scan started from this tab.")
        self.label.setObjectName(f"label_{prefix}_progress")
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        layout.addWidget(self.bar)
        layout.addWidget(self.label)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(FIRST_POLL_MS)
        self._cached = (None, None, None)  # (path, mtime, progress) so unchanged logs are not re-read

    def follow(self, pattern, newer_than, json_path=None):
        """Follow the newest log matching pattern written after newer_than; json_path supplies remove_angles."""
        self.log_pattern, self.newer_than, self.json_path, self.log_path = pattern, newer_than, json_path, None
        self._cached = (None, None, None)
        self._finished_sent = False
        self.timer.start(FIRST_POLL_MS)
        self.bar.setRange(0, 1)
        self.bar.setValue(0)
        self.refresh()

    def _skip_angles(self):
        try:
            with open(self.json_path) as f:
                return [float(a) for a in json.load(f).get("remove_angles") or []]
        except Exception:
            return []

    def _set_poll(self, p):
        if p["per_angle"] and p["current"] is not None:
            ms = int(p["per_angle"].total_seconds() * 1000 / POLL_FRACTION)
            ms = min(max(ms, MIN_POLL_MS), MAX_POLL_MS)
        else:
            ms = FIRST_POLL_MS if p["current"] is not None else MAX_POLL_MS
        if self.timer.interval() != ms:
            self.timer.setInterval(ms)

    def refresh(self):
        if self.log_pattern is None:
            return
        found = newest_log(self.log_pattern, self.newer_than)
        if found is None:
            self.label.setText("Waiting for the first angle to finish (no angle log yet).\n"
                               f"Checking every {self.timer.interval() // 1000} s.")
            return
        self.log_path = found
        try:
            mtime = os.path.getmtime(found)
            if self._cached[:2] == (found, mtime):
                p = self._cached[2]
            else:
                p = read_progress(found, self._skip_angles())
                self._cached = (found, mtime, p)
        except Exception as exc:
            self.label.setText(f"Cannot read {os.path.basename(found)}: {exc}")
            return
        self._set_poll(p)
        if p["current"] is None and p["done"] and not self._finished_sent:
            self._finished_sent = True
            self.finished.emit()
        self.bar.setRange(0, max(p["total"], 1))
        self.bar.setValue(p["done"])
        lines = [f"Angles: {p['done']} done, {p['total'] - p['done']} remaining  ({os.path.basename(found)})"]
        if p["current"] is None:
            lines.append("All angles done." if p["done"] else "No angles in the log.")
        else:
            lines.append(f"Current angle: {p['current']:.2f}\u00b0")
        if p["per_angle"]:
            lines.append(f"Time per angle: ~{_fmt(p['per_angle'])}")
        if p["finish"]:
            left = max(p["finish"] - datetime.now(), timedelta(0))
            lines.append(f"Estimated finish: {p['finish']:%a %H:%M}  (~{_fmt(left)} left)")
        if p["last_done"]:
            since = datetime.now() - p["last_done"]
            lines.append(f"Last angle finished: {p['last_done']:%H:%M}  ({_fmt(since)} ago)")
            if p["current"] is not None and p["per_angle"] and since > 3 * p["per_angle"]:
                lines.append("No new angle for a while: the scan may be paused, stopped or waiting for beam.")
        lines.append(f"Checking every {self.timer.interval() // 1000} s.")
        self.label.setText("\n".join(lines))
