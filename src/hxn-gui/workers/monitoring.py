"""
Monitoring and Generic Worker Threads

This module contains general-purpose monitoring threads for pressure plotting
and generic task execution.
Extracted from hxn_gui_v3.py for better modularity.

Author: Ajith Pattammattel
Refactored: 2026-04-15
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtTest
from epics import caget


class LivePressureMonitorThread(QThread):
    """
    Monitor pressure over time for real-time plotting.
    Emits time-pressure tuples at regular intervals.
    
    Signals:
        current_time_pressure (tuple): (time_ms, pressure_mmHg)
    """
    current_time_pressure = pyqtSignal(tuple)
    
    def __init__(self, pressure_pv, wait_time_ms=1000):
        """
        Initialize the live pressure monitor.
        
        Args:
            pressure_pv (str): EPICS PV for chamber pressure (mmHg)
            wait_time_ms (int): Sampling interval in milliseconds (default: 1000)
        """
        super().__init__()
        self.pressure_pv = pressure_pv
        self.wait_time = wait_time_ms
        self._running = True
    
    def run(self):
        """
        Main thread loop - continuously reads pressure and emits with timestamp.
        Time starts at 0 and increments by wait_time each iteration.
        """
        start_time = 0
        
        while self._running:
            try:
                current_pressure = caget(self.pressure_pv)
                if current_pressure is not None:
                    self.current_time_pressure.emit((start_time, current_pressure))
                
                QtTest.QTest.qWait(int(self.wait_time))
                start_time += self.wait_time
                
            except Exception as e:
                # Continue on error
                pass
    
    def stop(self):
        """Stop the monitoring thread."""
        self._running = False


class GenericWorkerThread(QThread):
    """
    Generic worker thread for executing arbitrary tasks in background.
    Useful for long-running operations that would block the GUI.
    
    Usage:
        worker = GenericWorkerThread(my_function, arg1, arg2, kwarg1=value1)
        worker.finished.connect(on_complete)
        worker.start()
    
    Signals:
        finished: Emitted when task completes
    """
    finished = pyqtSignal()
    
    def __init__(self, task, *args, **kwargs):
        """
        Initialize the worker with a task and its arguments.
        
        Args:
            task (callable): Function or method to execute
            *args: Positional arguments for the task
            **kwargs: Keyword arguments for the task
        """
        super().__init__()
        self.task = task
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        """
        Execute the task with provided arguments.
        Emits finished signal upon completion.
        """
        try:
            print(f"Executing task: {self.task.__name__}")
            self.task(*self.args, **self.kwargs)
            print(f"Task completed: {self.task.__name__}")
        except Exception as e:
            print(f"Error executing task: {e}")
        finally:
            self.finished.emit()
