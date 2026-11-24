"""QServer plan queue table: shows the running plan and queued plans; drag rows to reorder.

Polls RM.status() in a background thread and fetches RM.queue_get() only when the queue changes.
Moves and removals are sent to QServer, which stays the source of truth; the table is refreshed after.
"""
import json

from qtpy import QtCore, QtWidgets
from qtpy.QtCore import QThread, Qt, Signal

POLL_MS = 2000
COLUMNS = ("#", "Plan", "Arguments", "User", "Item UID")


def describe_item(item):
    """(plan name, argument text) for a queue item dict."""
    args = [json.dumps(a) if not isinstance(a, str) else a for a in item.get("args", [])]
    kwargs = [f"{k}={json.dumps(v) if not isinstance(v, str) else v}" for k, v in item.get("kwargs", {}).items()]
    return item.get("name", item.get("item_type", "?")), ", ".join(args + kwargs)


class QueuePoller(QThread):
    """Emits RM.queue_get() whenever the queue or running item changes."""
    queue = Signal(object)
    status = Signal(str)

    def __init__(self, rm, parent=None):
        super().__init__(parent)
        self.rm, self._key, self.force = rm, None, True

    def run(self):
        while not self.isInterruptionRequested():
            try:
                st = self.rm.status()
                key = (st.get("plan_queue_uid"), st.get("running_item_uid"))
                if self.force or key != self._key:
                    self.force, self._key = False, key
                    self.queue.emit(self.rm.queue_get())
            except Exception as exc:
                self._key = None
                self.status.emit(f"QServer unreachable: {exc}")
            for _ in range(POLL_MS // 100):
                if self.isInterruptionRequested() or self.force:
                    break
                self.msleep(100)


class QueueTree(QtWidgets.QTreeWidget):
    """Rows can be dragged to a new position but not dropped onto each other."""
    moved = Signal(str, str, str)  # uid, before_uid, after_uid ("" when not applicable)

    def dropEvent(self, event):
        # Work out the target from the drop position and let QServer reorder; the table is rebuilt
        # from the server afterwards, so Qt's own row move is not used.
        dragged = self.currentItem()
        event.setDropAction(Qt.IgnoreAction)
        event.accept()
        if dragged is None:
            return
        pos = event.position().toPoint() if hasattr(event, "position") else event.pos()
        target = self.itemAt(pos)
        uid = dragged.data(0, Qt.UserRole)
        if target is None:  # dropped below the last row
            last = self.topLevelItem(self.topLevelItemCount() - 1)
            if last is not None and last is not dragged:
                self.moved.emit(uid, "", last.data(0, Qt.UserRole))
            return
        if target is dragged:
            return
        rect = self.visualItemRect(target)
        if pos.y() < rect.center().y():
            self.moved.emit(uid, target.data(0, Qt.UserRole), "")
        else:
            self.moved.emit(uid, "", target.data(0, Qt.UserRole))


class QServerQueue(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rm, self.poller = None, None
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.label_running = QtWidgets.QLabel("Running: -")
        self.label_running.setObjectName("label_qserver_queue_running")
        self.label_running.setWordWrap(True)
        self.label_running.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(self.label_running)

        self.tree = QueueTree()
        self.tree.setObjectName("tw_qserver_queue")
        self.tree.setColumnCount(len(COLUMNS))
        self.tree.setHeaderLabels(COLUMNS)
        self.tree.setRootIsDecorated(False)
        self.tree.setAlternatingRowColors(True)
        self.tree.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tree.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tree.invisibleRootItem().setFlags(self.tree.invisibleRootItem().flags() | Qt.ItemIsDropEnabled)
        self.tree.moved.connect(self._move)
        layout.addWidget(self.tree, 1)

        row = QtWidgets.QHBoxLayout()
        self.buttons = {}
        for key, text, slot in (("up", "Move Up", lambda: self._step(-1)), ("down", "Move Down", lambda: self._step(1)),
                                ("remove", "Remove", self._remove), ("refresh", "Refresh", self.refresh)):
            b = QtWidgets.QPushButton(text)
            b.setObjectName(f"pb_qserver_queue_{key}")
            b.clicked.connect(slot)
            row.addWidget(b)
            self.buttons[key] = b
        self.label_status = QtWidgets.QLabel("Not connected.")
        self.label_status.setObjectName("label_qserver_queue_status")
        row.addWidget(self.label_status, 1)
        layout.addLayout(row)

    # ---- connection ----
    def start(self, rm):
        if rm is None:
            self.label_status.setText("RM (QServer API) is not defined in this session.")
            return
        self.stop()
        self.rm = rm
        self.poller = QueuePoller(rm, self)
        self.poller.queue.connect(self._show_queue)
        self.poller.status.connect(self.label_status.setText)
        self.poller.start()

    def stop(self):
        if self.poller is not None and self.poller.isRunning():
            self.poller.requestInterruption()
            self.poller.wait(3000)

    def refresh(self):
        if self.poller is not None:
            self.poller.force = True

    # ---- display ----
    def _show_queue(self, resp):
        running = resp.get("running_item") or {}
        if running:
            name, args = describe_item(running)
            self.label_running.setText(f"Running: {name}({args})")
        else:
            self.label_running.setText("Running: -")
        selected = self._selected_uid()
        self.tree.clear()
        for n, item in enumerate(resp.get("items", []), 1):
            name, args = describe_item(item)
            uid = item.get("item_uid", "")
            row = QtWidgets.QTreeWidgetItem([str(n), name, args, str(item.get("user", "")), uid[:8]])
            row.setData(0, Qt.UserRole, uid)
            row.setToolTip(2, args)
            row.setFlags((row.flags() | Qt.ItemIsDragEnabled) & ~Qt.ItemIsDropEnabled)
            self.tree.addTopLevelItem(row)
            if uid == selected:
                self.tree.setCurrentItem(row)
        for col in (0, 1, 3, 4):
            self.tree.resizeColumnToContents(col)
        n = self.tree.topLevelItemCount()
        self.label_status.setText(f"{n} plan(s) in the queue. Drag a row to change the order.")

    def _selected_uid(self):
        item = self.tree.currentItem()
        return item.data(0, Qt.UserRole) if item is not None else None

    # ---- actions (sent to QServer) ----
    def _call(self, what, fn, **kwargs):
        try:
            resp = fn(**kwargs)
            if isinstance(resp, dict) and resp.get("success") is False:
                raise RuntimeError(resp.get("msg", "request failed"))
            self.label_status.setText(f"{what}: done.")
        except Exception as exc:
            QtWidgets.QMessageBox.warning(self, "QServer Queue", f"{what} failed:\n{exc}")
        self.refresh()

    def _move(self, uid, before_uid, after_uid):
        kwargs = {"uid": uid, "before_uid": before_uid} if before_uid else {"uid": uid, "after_uid": after_uid}
        self._call("Move", self.rm.item_move, **kwargs)

    def _step(self, delta):
        item = self.tree.currentItem()
        if item is None or self.rm is None:
            return
        idx = self.tree.indexOfTopLevelItem(item)
        target = self.tree.topLevelItem(idx + delta)
        if target is None:
            return
        uid, other = item.data(0, Qt.UserRole), target.data(0, Qt.UserRole)
        self._move(uid, other, "") if delta < 0 else self._move(uid, "", other)

    def _remove(self):
        item = self.tree.currentItem()
        if item is None or self.rm is None:
            return
        choice = QtWidgets.QMessageBox.question(
            self, "Remove Plan", f"Remove plan {item.text(0)} ({item.text(1)}) from the QServer queue?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self._call("Remove", self.rm.item_remove, uid=item.data(0, Qt.UserRole))
