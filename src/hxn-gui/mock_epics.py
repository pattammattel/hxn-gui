"""
Mock EPICS module for offline testing
Provides dummy implementations of EPICS functions and hardware objects
"""

import logging
import random

log = logging.getLogger(__name__)

# Prevent real EPICS from being used
import os
os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'
os.environ['EPICS_CA_ADDR_LIST'] = ''

class MockMotor:
    """Mock motor object that simulates EPICS Motor behavior"""
    def __init__(self, name, initial_position=0.0):
        self.name = name
        self._position = initial_position
        self.connected = True
        self.prefix = f"Mock:{name}"
        log.info(f"MockMotor {name} created at position {initial_position}")
    
    @property
    def position(self):
        return self._position
    
    def move(self, target, wait=True, timeout=30.0):
        """Simulate motor movement"""
        log.info(f"MockMotor {self.name}: moving from {self._position} to {target}")
        self._position = target
        return True
    
    def get_position(self):
        return self._position


class MockDetector:
    """Mock detector object"""
    def __init__(self, name):
        self.name = name
        self.connected = True
        log.info(f"MockDetector {name} created")
    
    def __repr__(self):
        return f"MockDetector({self.name})"


# Cache for simulated PV values to provide consistent readings
_pv_cache = {}

def caget(pv_name, timeout=1.0):
    """Mock caget function - returns dummy values without connecting to EPICS"""
    # Return cached value if it exists, otherwise generate a reasonable default
    if pv_name in _pv_cache:
        # Add small random variation to simulate live readings
        base_value = _pv_cache[pv_name]
        if isinstance(base_value, (int, float)) and base_value > 1:
            return base_value + random.uniform(-0.01, 0.01) * base_value
        return base_value
    
    # Generate reasonable dummy values based on PV name patterns
    if 'IC' in pv_name or 'ch' in pv_name or 'cts' in pv_name:
        value = 10000.0  # Simulate ion chamber reading
    elif 'Sts' in pv_name or 'Status' in pv_name:
        value = 1  # Status OK
    elif 'Energy' in pv_name:
        value = 10.0  # keV
    elif 'Pressure' in pv_name or 'P-I' in pv_name:
        value = 1e-6  # Vacuum pressure
    elif 'ScanRunning' in pv_name:
        value = 0  # Not running
    elif 'ScanID' in pv_name:
        value = 12345  # Mock scan ID
    elif 'Pos-I' in pv_name or 'Mtr.RBV' in pv_name or 'Mtr.VAL' in pv_name:
        value = 0.0  # Motor position
    else:
        value = 0.0
    
    _pv_cache[pv_name] = value
    return value


def caput(pv_name, value, wait=False, timeout=30.0):
    """Mock caput function - simulates writing to PV"""
    log.debug(f"Mock caput: {pv_name} = {value}")
    _pv_cache[pv_name] = value
    return True


# Create mock motor objects (used in GUI)
zpssx = MockMotor('zpssx', 0.0)
zpssy = MockMotor('zpssy', 0.0)
zpssz = MockMotor('zpssz', 0.0)
dssx = MockMotor('dssx', 0.0)
dssy = MockMotor('dssy', 0.0)
dssz = MockMotor('dssz', 0.0)

# Mock detector strings (these are typically detector group names in bluesky)
dets_fast = "[fs, xspress3]"
dets_fast_merlin = "[fs, xspress3, merlin1]"
dets_fast_fs = "[fs]"

# Export Motor class for compatibility
Motor = MockMotor

log.info("="*60)
log.info("Mock EPICS module loaded - running in OFFLINE mode")
log.info("All hardware connections are simulated")
log.info("="*60)
