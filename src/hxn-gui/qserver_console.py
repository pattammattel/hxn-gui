"""Live copy of the QServer (RE Manager) console output in a GUI tab.

Requires the RE Manager to publish its console: start-re-manager ... --zmq-publish-console ON
(set in the run-queue-server script). Output printed before the GUI connects is not replayed.
"""
import time
from datetime import datetime

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import QThread, Signal

MAX_LINES = 5000
BATCH_S = 0.2  # send lines to the GUI at most this often


def split_console_text(buffer, text):
    """Add text to the pending buffer; return (complete lines, new buffer).

    A carriage return (progress bars such as tqdm) keeps only the text after it, so a
    redrawn progress line appears once, in its latest state.
    """
    buffer += text
    *lines, buffer = buffer.split("\n")
    return [line.rsplit("\r", 1)[-1] for line in lines], buffer


class ConsoleReader(QThread):
    """Reads RM.console_monitor in the background and emits batches of lines."""
    lines = Signal(list)
    status = Signal(str)

    def __init__(self, rm, parent=None):
        super().__init__(parent)
        self.rm = rm

    def run(self):
        monitor = self.rm.console_monitor
        try:
            monitor.enable()
        except Exception as exc:
            self.status.emit(f"Cannot start the console monitor: {exc}")
            return
        self.status.emit("Connected. Showing QServer output from now on "
                         "(needs --zmq-publish-console ON in run-queue-server).")
        buffer, batch, last_send = "", [], time.monotonic()
        try:
            while not self.isInterruptionRequested():
                try:
                    msg = monitor.next_msg(timeout=BATCH_S)
                    new, buffer = split_console_text(buffer, msg.get("msg", ""))
                    batch += new
                except Exception:
                    # Timeout: nothing new. Show a pending partial line (e.g. a prompt) as it is.
                    if buffer:
                        batch.append(buffer.rsplit("\r", 1)[-1])
                        buffer = ""
                if batch and (time.monotonic() - last_send >= BATCH_S or len(batch) > 500):
                    self.lines.emit(batch)
                    batch, last_send = [], time.monotonic()
            if batch:
                self.lines.emit(batch)
        finally:
            try:
                monitor.disable()
            except Exception:
                pass


class QServerConsole(QtWidgets.QWidget):
    """Read-only console view with Clear, Pause scrolling and Save buttons."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.reader = None
        layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QPlainTextEdit()
        self.text.setObjectName("pte_qserver_console")
        self.text.setReadOnly(True)
        self.text.setMaximumBlockCount(MAX_LINES)
        self.text.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.text.setFont(QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
        layout.addWidget(self.text)
        row = QtWidgets.QHBoxLayout()
        self.pb_clear = QtWidgets.QPushButton("Clear")
        self.pb_clear.setObjectName("pb_qserver_console_clear")
        self.pb_clear.clicked.connect(self.text.clear)
        self.pb_pause = QtWidgets.QPushButton("Pause Scrolling")
        self.pb_pause.setObjectName("pb_qserver_console_pause")
        self.pb_pause.setCheckable(True)
        self.pb_pause.toggled.connect(lambda on: self.pb_pause.setText("Resume Scrolling" if on else "Pause Scrolling"))
        self.pb_save = QtWidgets.QPushButton("Save to File...")
        self.pb_save.setObjectName("pb_qserver_console_save")
        self.pb_save.clicked.connect(self.save)
        self.label_status = QtWidgets.QLabel("Not connected.")
        self.label_status.setObjectName("label_qserver_console_status")
        for w in (self.pb_clear, self.pb_pause, self.pb_save):
            row.addWidget(w)
        row.addWidget(self.label_status, 1)
        layout.addLayout(row)

    def start(self, rm):
        if rm is None:
            self.label_status.setText("RM (QServer API) is not defined in this session.")
            return
        self.stop()
        self.reader = ConsoleReader(rm, self)
        self.reader.lines.connect(self.append_lines)
        self.reader.status.connect(self.label_status.setText)
        self.reader.start()

    def stop(self):
        if self.reader is not None and self.reader.isRunning():
            self.reader.requestInterruption()
            self.reader.wait(3000)

    def append_lines(self, lines):
        bar = self.text.verticalScrollBar()
        keep = bar.value()
        # Append at the end without moving the user's text cursor or selection.
        cursor = QtGui.QTextCursor(self.text.document())
        cursor.movePosition(QtGui.QTextCursor.End)
        for line in lines:
            if not self.text.document().isEmpty():
                cursor.insertBlock()
            cursor.insertText(line)
        if self.pb_pause.isChecked():
            bar.setValue(keep)
        else:
            bar.setValue(bar.maximum())

    def save(self):
        default = f"qserver_console_{datetime.now():%Y%m%d_%H%M%S}.txt"
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save QServer Console", default,
                                                        "Text files (*.txt);;All files (*)")
        if path:
            with open(path, "w") as f:
                f.write(self.text.toPlainText() + "\n")
            self.label_status.setText(f"Saved to {path}")
