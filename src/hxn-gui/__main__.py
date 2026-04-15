#!/usr/bin/env python
"""
HXN GUI - Main Application Entry Point

This is the refactored main entry point that will eventually replace hxn_gui_v3.py.
Currently a placeholder - full migration pending.

Usage:
    python -m hxn_gui
    # or
    ipython -m hxn_gui
"""

import sys
from PyQt5 import QtWidgets

# Eventually this will import from gui.main_window
# For now, import from the legacy file
from hxn_gui.hxn_gui_v3 import Ui


def main():
    """Main application entry point."""
    print("="*60)
    print("  HXN GUI - Hard X-ray Nanoprobe Beamline Control")
    print("  Version 4.0.0 (Refactored)")
    print("="*60)
    print()
    
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
