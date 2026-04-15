"""
Live Update Worker Threads

This module contains QThread workers for real-time PV monitoring and updates.
Extracted from hxn_gui_v3.py for better modularity.

Author: Ajith Pattammattel
Refactored: 2026-04-15
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtTest
from epics import caget


class LiveStatusThread(QThread):
    """
    Monitor a single EPICS PV status at regular intervals.
    
    Signals:
        current_sts (int): Emits the current PV value as integer
    """
    current_sts = pyqtSignal(int)
    
    def __init__(self, pv, update_interval_ms=500):
        """
        Initialize the live status monitor.
        
        Args:
            pv (str): EPICS PV address to monitor
            update_interval_ms (int): Update interval in milliseconds (default: 500)
        """
        super().__init__()
        self.pv = pv
        self.update_interval_ms = update_interval_ms
        self._running = True
    
    def run(self):
        """Main thread loop - continuously reads and emits PV value."""
        while self._running:
            try:
                value = caget(self.pv)
                if value is not None:
                    self.current_sts.emit(int(value))
                QtTest.QTest.qWait(self.update_interval_ms)
            except Exception as e:
                # Silently continue on error to prevent thread crash
                pass
    
    def stop(self):
        """Stop the monitoring thread."""
        self._running = False


class LiveUpdateThread(QThread):
    """
    Monitor multiple EPICS PVs and emit their values as a list.
    
    Signals:
        current_positions (list): Emits list of PV values in dictionary order
    """
    current_positions = pyqtSignal(list)
    
    def __init__(self, pv_dict, update_interval_ms=500):
        """
        Initialize the live update monitor.
        
        Args:
            pv_dict (dict): Dictionary mapping names to EPICS PV addresses
            update_interval_ms (int): Update interval in milliseconds (default: 500)
        """
        super().__init__()
        self.pv_dict = pv_dict
        self.update_interval_ms = update_interval_ms
        self._running = True
    
    def return_values(self):
        """
        Read all PV values from the dictionary.
        
        Returns:
            list: Current values of all PVs in dictionary order
        """
        readings = []
        for pv_address in self.pv_dict.values():
            try:
                value = caget(pv_address)
                readings.append(value if value is not None else 0.0)
            except Exception:
                readings.append(0.0)  # Default value on error
        return readings
    
    def run(self):
        """Main thread loop - continuously reads and emits all PV values."""
        while self._running:
            try:
                positions = self.return_values()
                self.current_positions.emit(positions)
                QtTest.QTest.qWait(self.update_interval_ms)
            except Exception as e:
                # Silently continue on error to prevent thread crash
                pass
    
    def stop(self):
        """Stop the monitoring thread."""
        self._running = False


class LiveThresholdUpdateThread(QThread):
    """
    Monitor a PV against a threshold and emit boolean status.
    Useful for alarm or limit monitoring.
    
    Signals:
        current_sts (bool): Emits True if PV > threshold, False otherwise
    """
    current_sts = pyqtSignal(bool)
    
    def __init__(self, pv, threshold, update_interval_ms=60000):
        """
        Initialize the threshold monitor.
        
        Args:
            pv (str): EPICS PV address to monitor
            threshold (float): Threshold value for comparison
            update_interval_ms (int): Update interval in milliseconds (default: 60000)
        """
        super().__init__()
        self.pv = pv
        self.threshold = threshold
        self.update_interval_ms = update_interval_ms
        self._running = True
    
    def run(self):
        """Main thread loop - checks PV against threshold."""
        while self._running:
            try:
                value = caget(self.pv)
                if value is not None:
                    exceeds_threshold = value > self.threshold
                    self.current_sts.emit(exceeds_threshold)
                QtTest.QTest.qWait(self.update_interval_ms)
            except Exception as e:
                # Silently continue on error
                pass
    
    def stop(self):
        """Stop the monitoring thread."""
        self._running = False
