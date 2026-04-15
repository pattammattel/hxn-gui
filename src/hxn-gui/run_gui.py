#!/usr/bin/env python
"""
HXN GUI Launcher

Entry point script for launching the HXN GUI application.
This script can be run directly or via ipython.

Usage:
    python run_gui.py
    ipython run_gui.py
    ipython -i run_gui.py  # Interactive mode

Author: Ajith Pattammattel
"""

import sys
import os

# Ensure the package is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the GUI
if __name__ == "__main__":
    from PyQt5 import QtWidgets
    from hxn_gui_v3 import Ui
    
    print("="*60)
    print("  HXN GUI - Hard X-ray Nanoprobe Beamline Control")
    print("  Version 4.0 (Refactored Architecture)")
    print("="*60)
    print()
    
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
