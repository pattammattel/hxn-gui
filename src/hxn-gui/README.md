# HXN GUI - Refactored Package Structure

A modular PyQt5-based graphical user interface for the Hard X-ray Nanoprobe (HXN) beamline at NSLS-II.

**Author:** Ajith Pattammattel  
**Refactored:** April 15, 2026  
**Version:** 4.0.0

## Quick Start

```bash
# Your original command still works!
ipython hxn_gui_v3.py

# Or use the new launcher (recommended)
ipython run_gui.py
```

**See [HOW_TO_RUN.md](HOW_TO_RUN.md) for all running options.**

## Overview

This package has been refactored from a monolithic 2,887-line file into a well-organized, modular architecture for improved maintainability, testability, and extensibility.

## Package Structure

```
hxn_gui/
├── __init__.py                     # Package entry point with version info
├── README.md                       # This file
│
├── config/                         # Configuration & Constants
│   ├── __init__.py
│   ├── constants.py               # All hardcoded values, PV addresses
│   └── settings.py                # User settings & secure credentials
│
├── workers/                        # Background Thread Workers
│   ├── __init__.py
│   ├── live_updates.py            # PV monitoring threads
│   ├── scan_progress.py           # Scan progress tracking
│   ├── chamber_ops.py             # Vacuum chamber operations
│   └── monitoring.py              # Pressure monitoring & generic workers
│
├── controllers/                    # Domain Controllers (planned)
│   └── __init__.py                # To be populated from hxn_gui_v3.py
│
├── gui/                           # GUI Components (planned)
│   └── __init__.py                # To be populated from hxn_gui_v3.py
│
├── utils/                         # Utility Functions
│   ├── __init__.py
│   ├── utilities.py               # General utilities (existing)
│   └── element_lines.py           # XRF elements (existing)
│
├── core/                          # Core Beamline Functionality
│   ├── __init__.py
│   ├── HXNSampleExchange.py       # Sample exchange protocol (existing)
│   └── hxn_data_transfer.py       # Data transfer utilities (existing)
│
├── ui_files/                      # Qt UI Files
│   └── *.ui                       # Qt Designer UI files
│
├── json_plans/                    # JSON Plan Makers
│   └── *.py                       # Various plan generators
│
└── Archieved/                     # Legacy Files
    └── *.py                       # Old versions for reference
```

## Key Improvements

### 1. **Security Enhancement** ✅
- **Removed hardcoded credentials** from source code
- Credentials now loaded from environment variables
- Usage:
  ```bash
  export HXN_GITHUB_TOKEN="your_token_here"
  ```

### 2. **Modular Worker Threads** ✅
Extracted 8 QThread classes into dedicated modules:
- `LiveStatusThread` - Single PV monitoring
- `LiveUpdateThread` - Multiple PV monitoring
- `LiveThresholdUpdateThread` - Threshold-based monitoring
- `ScanProgressThread` - Scan progress tracking
- `PumpingThread` - Chamber pumping control
- `VentingThread` - Chamber venting control
- `HeBackfillThread` - Helium backfill control
- `LivePressureMonitorThread` - Real-time pressure plotting
- `GenericWorkerThread` - Generic task execution

### 3. **Centralized Configuration** ✅
All constants moved to `config/constants.py`:
- File paths and directories
- Detector configurations
- Default positions
- Pressure thresholds
- Scan presets
- EPICS PV addresses
- Validation patterns

User-configurable settings in `config/settings.py`:
- Microscope mode (ZP/MLL)
- Update intervals
- Confirmation preferences
- Logging settings

### 4. **Improved Code Organization** ✅
- **Before:** 1 file with 2,887 lines, 11 classes
- **After:** Organized into 20+ focused modules
- Clear separation of concerns
- Better discoverability

### 5. **Better Documentation**
- Comprehensive docstrings for all classes
- Type hints where applicable
- Module-level documentation
- Usage examples

## Migration Guide

### Importing Workers

**Before:**
```python
# Workers were embedded in main file
from hxn_gui_v3 import liveUpdate, PumpingThread
```

**After:**
```python
# Import from dedicated package
from hxn_gui.workers import LiveUpdateThread, PumpingThread
```

### Using Configuration

**Before:**
```python
# Hardcoded in file
MAX_SCAN_POINTS = 64000
VORTEX_OUT_POSITION = -107.0
```

**After:**
```python
# Import from config
from hxn_gui.config.constants import MAX_SCAN_POINTS, VORTEX_OUT_POSITION
```

### Settings Management

**Before:**
```python
# No centralized settings management
```

**After:**
```python
from hxn_gui.config.settings import settings

# Get setting
mode = settings.get('microscope_mode')

# Update setting
settings.set('microscope_mode', 'mll')
```

## Running the Application

The original `hxn_gui_v3.py` can still be run as before (currently unchanged):

```bash
python hxn_gui_v3.py
```

## Next Steps (Planned)

The following refactorings are planned for future iterations:

### Phase 2: Extract Controllers
1. `controllers/flyscan.py` - Fly scan control methods
2. `controllers/stage_navigator.py` - Motor movement methods
3. `controllers/energy_manager.py` - Energy management
4. `controllers/detector_manager.py` - Detector control
5. `controllers/alignment_tools.py` - Alignment utilities
6. `controllers/sample_pos_manager.py` - Position management
7. `controllers/vacuum_control.py` - Vacuum operations
8. `controllers/user_manager.py` - User setup
9. `controllers/queue_manager.py` - QServer integration
10. `controllers/plotting_tools.py` - Visualization
11. `controllers/pdf_logger.py` - PDF generation

### Phase 3: Refactor Main GUI
1. Extract main `Ui` class to `gui/main_window.py`
2. Reduce main window to orchestration logic (~600 lines)
3. Delegate functionality to controllers
4. Implement proper MVC/MVP pattern

### Phase 4: Testing & Documentation
1. Add unit tests for workers
2. Add integration tests for controllers
3. Add comprehensive API documentation
4. Create developer guide

## Benefits of Refactoring

1. **Maintainability:** Easier to locate and modify specific functionality
2. **Testability:** Isolated modules are easier to test
3. **Reusability:** Workers and controllers can be used independently
4. **Scalability:** New features can be added without modifying core
5. **Security:** Credentials managed securely via environment
6. **Collaboration:** Multiple developers can work on different modules
7. **Documentation:** Better code organization improves documentation

## Dependencies

- Python 3.10+
- PyQt5
- pyqtgraph
- EPICS/pyepics
- BlueSky/Ophyd
- matplotlib
- numpy

## Environment Setup

Create settings directory (automatically created on first run):
```bash
~/.hxn_gui/settings.json
```

Set environment variables for credentials:
```bash
export HXN_GITHUB_TOKEN="your_token_here"
```

## Contributing

When adding new features:
1. Identify the appropriate module/package
2. Follow existing naming conventions
3. Add comprehensive docstrings
4. Update `__all__` exports in `__init__.py`
5. Document in this README if significant

## License

NSLS-II Beamline Software

---

**Questions?** Contact Ajith Pattammattel
