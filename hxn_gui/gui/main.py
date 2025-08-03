import sys
import logging
from PyQt6 import QtWidgets
from .windows.hxn_gui_window import hxn_guiWindow
from . import UI_DIR

def start_hxn_gui():
    # configure logging…
    app = QtWidgets.QApplication(sys.argv)

    # Apply stylesheet if exists
    qss_file = UI_DIR / "css" / "uswds.qss"
    if qss_file.exists():
        with open(qss_file, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

    win = hxn_guiWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    start_hxn_gui()
