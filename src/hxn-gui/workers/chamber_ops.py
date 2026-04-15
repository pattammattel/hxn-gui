"""
Chamber Operations Worker Threads

This module contains QThread workers for vacuum chamber operations including
pumping, venting, and helium backfill processes.
Extracted from hxn_gui_v3.py for better modularity.

Author: Ajith Pattammattel
Refactored: 2026-04-15
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtTest
from epics import caget


class PumpingThread(QThread):
    """
    Control chamber pumping sequence (slow pump -> fast pump -> target pressure).
    Monitors pressure and triggers fast pump when appropriate.
    
    Signals:
        pressure_change (int): Progress percentage (0-100)
        start_slow_pump: Trigger to start slow pump
        start_fast_pump: Trigger to start fast pump
        finished: Emitted when target pressure reached
    """
    pressure_change = pyqtSignal(int)
    start_slow_pump = pyqtSignal()
    start_fast_pump = pyqtSignal()
    finished = pyqtSignal()
    
    def __init__(self, pressure_pv, fast_pump_start_pressure, target_pressure):
        """
        Initialize the pumping controller.
        
        Args:
            pressure_pv (str): EPICS PV for chamber pressure (mmHg)
            fast_pump_start_pressure (float): Pressure to trigger fast pump (mmHg)
            target_pressure (float): Target final pressure (mmHg)
        """
        super().__init__()
        self.pressure_pv = pressure_pv
        self.fast_pump_start_p = fast_pump_start_pressure
        self.target_p = target_pressure
        self._running = True
    
    def run(self):
        """
        Execute pumping sequence:
        1. Start slow pump
        2. Wait until fast pump trigger pressure
        3. Start fast pump
        4. Wait until target pressure
        """
        try:
            # Start slow pump
            self.start_slow_pump.emit()
            
            # If we need to reach pressure below fast pump trigger
            if self.target_p < self.fast_pump_start_p:
                # Wait for slow pump to reach trigger pressure
                while self._running and caget(self.pressure_pv) > self.fast_pump_start_p:
                    current_pressure = caget(self.pressure_pv)
                    # Calculate progress (760 mmHg atmospheric to 0)
                    progress = int((760 - current_pressure) / 7.6)
                    self.pressure_change.emit(progress)
                    QtTest.QTest.qWait(5000)  # Update every 5 seconds
                
                if self._running:
                    # Trigger fast pump
                    self.start_fast_pump.emit()
                    print("Fast pump triggered")
            
            # Wait for target pressure
            while self._running and caget(self.pressure_pv) > self.target_p:
                current_pressure = caget(self.pressure_pv)
                progress = int((760 - current_pressure) / 7.6)
                self.pressure_change.emit(progress)
                QtTest.QTest.qWait(5000)
            
            if self._running:
                self.finished.emit()
                
        except Exception as e:
            print(f"Error during pumping: {e}")
            self.finished.emit()
    
    def stop(self):
        """Stop the pumping sequence."""
        self._running = False


class VentingThread(QThread):
    """
    Control chamber venting to atmospheric pressure.
    
    Signals:
        pressure_change (int): Current pressure in mmHg
        open_vent: Trigger to open vent valve
        finished: Emitted when target pressure reached
    """
    pressure_change = pyqtSignal(int)
    open_vent = pyqtSignal()
    finished = pyqtSignal()
    
    def __init__(self, pressure_pv, target_pressure):
        """
        Initialize the venting controller.
        
        Args:
            pressure_pv (str): EPICS PV for chamber pressure (mmHg)
            target_pressure (float): Target atmospheric pressure (mmHg, typically 760)
        """
        super().__init__()
        self.pressure_pv = pressure_pv
        self.target_p = target_pressure
        self._running = True
        print(f"Venting target: {self.target_p} mmHg")
    
    def run(self):
        """
        Execute venting sequence:
        1. Open vent valve
        2. Monitor pressure increase to atmospheric
        """
        try:
            # Open vent valve
            self.open_vent.emit()
            
            # Wait for pressure to reach atmospheric
            while self._running and caget(self.pressure_pv) < self.target_p:
                current_pressure = caget(self.pressure_pv)
                self.pressure_change.emit(int(current_pressure))
                QtTest.QTest.qWait(5000)  # Update every 5 seconds
            
            if self._running:
                self.finished.emit()
                
        except Exception as e:
            print(f"Error during venting: {e}")
            self.finished.emit()
    
    def stop(self):
        """Stop the venting sequence."""
        self._running = False


class HeBackfillThread(QThread):
    """
    Control helium backfill to specified pressure.
    Used for sample exchange under inert atmosphere.
    
    Signals:
        pressure_change (int): Current pressure in mmHg
        start_he_backfill: Trigger to start helium flow
        finished: Emitted when target pressure reached
    """
    pressure_change = pyqtSignal(int)
    start_he_backfill = pyqtSignal()
    finished = pyqtSignal()
    
    def __init__(self, pressure_pv, target_pressure):
        """
        Initialize the helium backfill controller.
        
        Args:
            pressure_pv (str): EPICS PV for chamber pressure (mmHg)
            target_pressure (float): Target He pressure (mmHg, typically ~250)
        """
        super().__init__()
        self.pressure_pv = pressure_pv
        self.target_p = target_pressure
        self._running = True
    
    def run(self):
        """
        Execute helium backfill sequence:
        1. Start helium flow
        2. Monitor pressure increase to target
        """
        try:
            # Start helium backfill
            self.start_he_backfill.emit()
            
            # Wait for pressure to reach ~248 mmHg (just before target)
            while self._running and caget(self.pressure_pv) < 248.0:
                current_pressure = caget(self.pressure_pv)
                self.pressure_change.emit(int(current_pressure))
                QtTest.QTest.qWait(1000)  # Update every second
            
            if self._running:
                self.finished.emit()
                
        except Exception as e:
            print(f"Error during helium backfill: {e}")
            self.finished.emit()
    
    def stop(self):
        """Stop the backfill sequence."""
        self._running = False
