"""
Scan Progress Worker Thread

This module contains the QThread worker for monitoring scan progress.
Extracted from hxn_gui_v3.py for better modularity.

Author: Ajith Pattammattel
Refactored: 2026-04-15
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtTest
from epics import caget


class ScanProgressThread(QThread):
    """
    Monitor scan progress by tracking completed vs total scan points.
    Emits updates until scan completes, then automatically terminates.
    
    Signals:
        tot_scan_points (int): Emitted once at start with total scan points
        completed_points (int): Emitted periodically with completed points count
        finished: Emitted when scan completes (tot == completed)
    """
    tot_scan_points = pyqtSignal(int)
    completed_points = pyqtSignal(int)
    
    def __init__(self, total_pv, completed_pv, update_interval_ms=100):
        """
        Initialize the scan progress monitor.
        
        Args:
            total_pv (str): EPICS PV for total scan points
            completed_pv (str): EPICS PV for completed scan points
            update_interval_ms (int): Update interval in milliseconds (default: 100)
        """
        super().__init__()
        self.total_pv = total_pv
        self.completed_pv = completed_pv
        self.update_interval_ms = update_interval_ms
    
    def run(self):
        """
        Main thread loop - monitors scan progress until completion.
        Automatically exits when scan completes.
        """
        try:
            # Emit total scan points at start
            total_points = caget(self.total_pv)
            if total_points is not None:
                self.tot_scan_points.emit(int(total_points))
            else:
                total_points = 0
            
            # Monitor progress
            while True:
                completed = caget(self.completed_pv)
                
                if completed is not None:
                    completed_int = int(completed)
                    self.completed_points.emit(completed_int)
                    
                    # Check if scan is complete
                    if total_points > 0 and completed_int >= total_points:
                        break
                
                QtTest.QTest.qWait(self.update_interval_ms)
            
            # Emit finished signal
            self.finished.emit()
            
        except Exception as e:
            print(f"Error in scan progress monitor: {e}")
            self.finished.emit()
