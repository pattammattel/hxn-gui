# HXN GUI Refactoring - Migration Guide

This document provides step-by-step instructions for migrating the existing `hxn_gui_v3.py` to use the refactored package structure.

## Phase 1: Update Imports (Immediate Changes)

### Step 1: Remove Security Issue

**Current (line 5):**
```python
_ethanu_ente!_$thakkol_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
```

**Action:** Delete this line and set environment variable instead:
```bash
export HXN_GITHUB_TOKEN="your_actual_token_here"
```

### Step 2: Clean Up Duplicate Imports

**Current (lines 8, 13):**
```python
import sys      # Line 8
...
import sys      # Line 13 - DUPLICATE!
```

**Action:** Remove the duplicate on line 13.

### Step 3: Update Worker Thread Imports

**Current:**
```python
# Workers defined in same file (lines 2600-2887)
class liveStatus(QThread):
    ...
class liveUpdate(QThread):
    ...
# etc.
```

**New:**
```python
# Import from workers package
from hxn_gui.workers import (
    LiveStatusThread,        # Renamed from liveStatus
    LiveUpdateThread,        # Renamed from liveUpdate  
    LiveThresholdUpdateThread,  # Renamed from liveThresholdUpdate
    ScanProgressThread,      # Renamed from updateScanProgress
    PumpingThread,
    VentingThread,
    HeBackfillThread,
    LivePressureMonitorThread,  # Renamed from LivePressureValueThread
    GenericWorkerThread      # Renamed from WorkerThread
)
```

**Changes Required in Code:**
- Replace `liveStatus(` → `LiveStatusThread(`
- Replace `liveUpdate(` → `LiveUpdateThread(`
- Replace `liveThresholdUpdate(` → `LiveThresholdUpdateThread(`
- Replace `updateScanProgress(` → `ScanProgressThread(`
- Replace `LivePressureValueThread(` → `LivePressureMonitorThread(`
- Replace `WorkerThread(` → `GenericWorkerThread(`

### Step 4: Update Module Imports

**Current:**
```python
from HXNSampleExchange import *
from hxn_data_transfer import *
HXNSampleExchanger = SampleExchangeProtocol()
from utilities import *
from element_lines import *
from mll_tomo_gui import *
```

**New:**
```python
from hxn_gui.core.HXNSampleExchange import *
from hxn_gui.core.hxn_data_transfer import *
from hxn_gui.core import SampleExchangeProtocol
HXNSampleExchanger = SampleExchangeProtocol()
from hxn_gui.utils.utilities import *
from hxn_gui.utils.element_lines import *
from mll_tomo_gui import *  # Keep as is - external module
```

### Step 5: Add Configuration Imports

**Add at top after other imports:**
```python
from hxn_gui.config import constants as cfg
from hxn_gui.config.settings import settings
```

### Step 6: Update Path Handling

**Current:**
```python
ui_path = os.path.dirname(os.path.abspath(__file__))
style_path = os.path.join(os.path.dirname(ui_path),'uswds_style.qss')
```

**New:**
```python
# Use constants from config
from hxn_gui.config.constants import UI_FILE_V3, STYLE_FILE
ui_path = os.path.dirname(os.path.abspath(__file__))  # Keep for compatibility
```

### Step 7: Update Constants Usage

**Current:**
```python
det_and_camera_names_motion = ['cam11','merlin','eiger']
det_and_camera_names_data = ['cam11','merlin1','merlin2','eiger1']
```

**New:**
```python
from hxn_gui.config.constants import (
    DET_CAMERA_NAMES_MOTION,
    DET_CAMERA_NAMES_DATA
)
det_and_camera_names_motion = DET_CAMERA_NAMES_MOTION
det_and_camera_names_data = DET_CAMERA_NAMES_DATA
```

## Phase 2: Update UI Loading

**Current:**
```python
uic.loadUi(os.path.join(ui_path,'ui_files/hxn_gui_v3.ui'), self)
```

**New:**
```python
from hxn_gui.config.constants import UI_FILE_V3
uic.loadUi(UI_FILE_V3, self)
```

## Phase 3: Update Scan Presets

**Current:**
```python
# Hardcoded in fill_common_scan_params()
# (20, 20, 100, 100, 0.005)
```

**New:**
```python
from hxn_gui.config.constants import SCAN_PRESETS

# In fill_common_scan_params():
preset = SCAN_PRESETS['20x20']  # (20, 20, 100, 100, 0.005)
```

## Phase 4: Update Thread Instantiations

### Example 1: liveUpdateThread

**Current:**
```python
def liveUpdateThread(self):
    self.live_update_thread = liveUpdate(self.live_pv_dict, 500)
    self.live_update_thread.current_positions.connect(self.handle_value_signals)
    self.live_update_thread.start()
```

**New:**
```python
def liveUpdateThread(self):
    from hxn_gui.workers import LiveUpdateThread
    self.live_update_thread = LiveUpdateThread(self.live_pv_dict, 500)
    self.live_update_thread.current_positions.connect(self.handle_value_signals)
    self.live_update_thread.start()
```

### Example 2: start_pumping_in_thread

**Current:**
```python
def start_pumping_in_thread(self):
    ...
    self.pumping_thread = PumpingThread(pressure_pv, fast_pump_start_p, target_p)
    self.pumping_thread.pressure_change.connect(...)
    self.pumping_thread.start()
```

**New:**
```python
def start_pumping_in_thread(self):
    from hxn_gui.workers import PumpingThread
    from hxn_gui.config.constants import PRESSURE_FAST_PUMP_TRIGGER, PRESSURE_VACUUM_TARGET
    ...
    self.pumping_thread = PumpingThread(pressure_pv, PRESSURE_FAST_PUMP_TRIGGER, target_p)
    self.pumping_thread.pressure_change.connect(...)
    self.pumping_thread.start()
```

## Phase 5: Add Settings Integration

### Example: Use settings for update intervals

**Current:**
```python
self.live_update_thread = LiveUpdateThread(self.live_pv_dict, 500)  # Hardcoded
```

**New:**
```python
from hxn_gui.config.settings import settings
interval = settings.get('live_update_interval_ms', 500)
self.live_update_thread = LiveUpdateThread(self.live_pv_dict, interval)
```

## Quick Reference: Class Name Changes

| Old Name | New Name | Module |
|----------|----------|--------|
| `liveStatus` | `LiveStatusThread` | `workers.live_updates` |
| `liveUpdate` | `LiveUpdateThread` | `workers.live_updates` |
| `liveThresholdUpdate` | `LiveThresholdUpdateThread` | `workers.live_updates` |
| `updateScanProgress` | `ScanProgressThread` | `workers.scan_progress` |
| `PumpingThread` | `PumpingThread` | `workers.chamber_ops` |
| `VentingThread` | `VentingThread` | `workers.chamber_ops` |
| `HeBackFillThread` | `HeBackfillThread` | `workers.chamber_ops` |
| `LivePressureValueThread` | `LivePressureMonitorThread` | `workers.monitoring` |
| `WorkerThread` | `GenericWorkerThread` | `workers.monitoring` |

## Search & Replace Guide

Use your IDE's search and replace function:

1. **Remove old thread class definitions** (lines 2600-2887)
   - Search: `^class (liveStatus|liveUpdate|.*Thread).*:$` (regex)
   - Action: Delete these class definitions (they're in workers/ now)

2. **Update thread instantiations:**
   ```
   Find: liveStatus\(          Replace: LiveStatusThread(
   Find: liveUpdate\(          Replace: LiveUpdateThread(
   Find: liveThresholdUpdate\( Replace: LiveThresholdUpdateThread(
   Find: updateScanProgress\(  Replace: ScanProgressThread(
   Find: LivePressureValueThread\( Replace: LivePressureMonitorThread(
   Find: WorkerThread\(        Replace: GenericWorkerThread(
   ```

3. **Update imports:**
   - Add at top of file:
   ```python
   from hxn_gui.workers import (
       LiveStatusThread,
       LiveUpdateThread,
       LiveThresholdUpdateThread,
       ScanProgressThread,
       PumpingThread,
       VentingThread,
       HeBackfillThread,
       LivePressureMonitorThread,
       GenericWorkerThread
   )
   from hxn_gui.config import constants as cfg
   from hxn_gui.config.settings import settings
   ```

## Testing After Migration

1. **Start the GUI and verify:**
   - UI loads correctly
   - Live PV updates work
   - Scan progress monitoring works
   - Chamber operations work (pumping, venting)
   - No import errors in console

2. **Test each refactored component:**
   - Run a fly scan (tests ScanProgressThread)
   - Monitor live positions (tests LiveUpdateThread)
   - Run pumping sequence (tests PumpingThread)

3. **Check for any remaining issues:**
   ```bash
   # Look for old class names
   grep -n "class liveStatus" hxn_gui_v3.py
   grep -n "class liveUpdate" hxn_gui_v3.py
   ```

## Rollback Plan

If issues arise, the original file is preserved:
```bash
# Original (before refactoring)
git checkout HEAD~1 hxn_gui_v3.py
```

Or keep a backup:
```bash
cp hxn_gui_v3.py hxn_gui_v3.py.backup
```

## Contact

For questions about this migration, contact the refactoring team or refer to:
- `README.md` - Package overview
- `config/constants.py` - All constants
- `workers/__init__.py` - Worker class documentation
