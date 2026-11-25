"""QMonitor-style QServer tab built from the bluesky-widgets panels, plus the live console.

Layout (as QMonitor's "Edit and Control Queue" view, without the Connect button):
  top:    Environment | Queue | Plan Execution | RE Manager Status | extras (destroy env, save history)
  bottom: [Plan Viewer/Editor over Queue] | [Running Plan over History] | [Console]
The connection is automatic: a background thread polls QServer once a second, as QMonitor does after
Connect, and keeps retrying while QServer is down.
"""
import os

from qtpy import QtCore, QtWidgets
from qtpy.QtCore import QThread, Qt, Signal

import bluesky_widgets_compat  # noqa: F401  (PyQt6 fixes; must come before the widgets are built)
from bluesky_widgets.models.run_engine_client import RunEngineClient
from bluesky_widgets.qt.run_engine_client import (
    QtReEnvironmentControls,
    QtReExecutionControls,
    QtRePlanEditor,
    QtRePlanHistory,
    QtRePlanQueue,
    QtReQueueControls,
    QtReRunningPlan,
    QtReStatusMonitor,
)

from qserver_console import QServerConsole

UPDATE_PERIOD_MS = 1000
STOP_WAIT_MS = 6000  # one QServer request timeout plus margin


class StatusPoller(QThread):
    """Refreshes the model status every second; loads queue, history and allowed plans/devices once
    QServer first answers (as QMonitor does on Connect). While QServer is down each pass waits for one
    request timeout (about 2 s), so stopping can take that long."""

    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model

    def run(self):
        loaded = False
        while not self.isInterruptionRequested():
            try:
                self.model.load_re_manager_status()
                if self.model._re_manager_connected and not loaded:
                    self.model.manager_connecting_ops()
                    loaded = True
            except Exception as exc:
                print(f"[QSERVER] update failed, retrying: {exc}")
            for _ in range(UPDATE_PERIOD_MS // 100):
                if self.isInterruptionRequested():
                    return
                self.msleep(100)


class QServerMonitor(QtWidgets.QWidget):
    status_changed = Signal()  # model events come from the poller thread; delivered on the GUI thread

    def __init__(self, rm=None, parent=None):
        super().__init__(parent)
        self.model = RunEngineClient()  # default 0MQ addresses, same as the GUI's RM
        self.poller = None
        self._work_dir = os.path.expanduser("~")
        m = self.model

        top = QtWidgets.QHBoxLayout()
        for w in (QtReEnvironmentControls(m), QtReQueueControls(m), QtReExecutionControls(m), QtReStatusMonitor(m)):
            top.addWidget(w)
        top.addWidget(self._build_extras())
        top.addStretch()

        editor, queue = QtRePlanEditor(m), QtRePlanQueue(m)
        queue.registered_item_editors.append(editor.edit_queue_item)  # double-click a plan to edit it
        self.console = QServerConsole()

        def column(*widgets, sizes):
            split = QtWidgets.QSplitter(Qt.Vertical)
            for w in widgets:
                split.addWidget(w)
            split.setSizes(sizes)
            return split

        body = QtWidgets.QSplitter(Qt.Horizontal)
        body.setObjectName("splitter_qserver")
        body.addWidget(column(editor, queue, sizes=[1, 1]))
        body.addWidget(column(QtReRunningPlan(m), QtRePlanHistory(m), sizes=[1, 2]))
        body.addWidget(self.console)
        body.setSizes([1, 1, 1])

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(top)
        layout.addWidget(body, 1)
        self._rm = rm
        self.status_changed.connect(self._update_destroy_state)
        m.events.status_changed.connect(lambda event: self.status_changed.emit())

    def _build_extras(self):
        # QMonitor's "Control Actions" and "Save and Backup" menus, as buttons.
        box = QtWidgets.QGroupBox("Options")
        vbox = QtWidgets.QVBoxLayout(box)
        self.cb_destroy = QtWidgets.QCheckBox("Allow Destroy")
        self.cb_destroy.setObjectName("cb_qserver_allow_destroy")
        self.cb_destroy.toggled.connect(self.model.activate_env_destroy)
        self.pb_save_history = QtWidgets.QPushButton("Save History")
        self.pb_save_history.setObjectName("pb_qserver_save_history")
        menu = QtWidgets.QMenu(self.pb_save_history)
        for fmt in ("txt", "json", "yaml"):
            menu.addAction(f"as .{fmt}", lambda f=fmt: self._save_history(f))
        self.pb_save_history.setMenu(menu)
        vbox.addWidget(self.cb_destroy)
        vbox.addWidget(self.pb_save_history)
        vbox.addStretch()
        return box

    def _update_destroy_state(self):
        with QtCore.QSignalBlocker(self.cb_destroy):
            self.cb_destroy.setChecked(bool(self.model.env_destroy_activated))

    def _save_history(self, fmt):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Plan History", os.path.join(self._work_dir, f"plan_history.{fmt}"),
            f"{fmt.upper()} (*.{fmt});;All (*)")
        if not path:
            return
        try:
            self.model.save_plan_history_to_file(file_path=path, file_format=fmt)
            self._work_dir = os.path.dirname(path)
        except Exception as exc:
            QtWidgets.QMessageBox.warning(self, "Save Plan History", f"Failed to save: {exc}")

    def start(self):
        self.model.clear_connection_status()
        self.poller = StatusPoller(self.model, self)
        self.poller.start()
        self.console.start(self._rm)

    def stop(self):
        if self.poller is not None and self.poller.isRunning():
            self.poller.requestInterruption()
            self.poller.wait(STOP_WAIT_MS)
        self.console.stop()
