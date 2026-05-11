# HXN GUI Refactoring Plan

## Current State
- **File:** `src/hxn-gui/hxn_gui_v3.py`
- **Size:** 3,075 lines
- **Structure:** Single monolithic class `Ui` with all functionality

## Goals
1. Improve code maintainability and readability
2. Enable easier testing
3. Reduce cognitive load when working on specific features
4. Keep functionality intact (verify with offline mode after each step)

## Refactoring Strategy: Extract Feature Modules

We'll extract logical groups of functionality into separate mixin classes or handler modules, one at a time.

---

## Phase 1: Extract Motor Control Classes ✓ IN PROGRESS

### Step 1.1: Extract ZP Stage Controller ✓ COMPLETE
**Status:** ✅ Completed
**Commit:** `a313542` - "refactor: extract ZP stage controller into separate module"
**File:** `src/hxn-gui/controllers/zp_stage_controller.py` (110 lines)
**Main file:** Reduced from 3,075 to 3,004 lines (71 lines extracted)

**Extracted methods:**
- `connect_zp_stages()` - Signal connections for ZP stage controls
- `move_smarx()`, `move_smary()`, `move_smarz()` - Sample stage movements
- `move_zpth()`, `move_zpz1()` - Rotation and focus stage movements
- `zp_to_cam11_view_()`, `zp_to_nanobeam_()` - Configuration presets
- `ZP_OSA_OUT()`, `ZP_OSA_IN()` - Order Sorting Aperture control
- `ZP_BS_OUT()`, `ZP_BS_IN()` - Beamstop control

**Integration:** Using mixin pattern - `class Ui(QtWidgets.QMainWindow, Ui_window, ZPStageController)`

**Testing checklist:**
- [x] Syntax check passed
- [ ] Import in offline mode works
- [ ] ZP stage movement buttons connect properly
- [ ] OSA/BS controls work
- [ ] Configuration presets (cam11, nanobeam) work
- [ ] Error decorators function correctly

**Next:** Test in offline mode before proceeding to Step 1.2

---

### Step 1.2: Extract MLL Stage Controller ⏳ READY TO START
**Target:** ~150 lines
**Methods to extract:**
- `connect_zp_stages()`
- `move_smarx()`, `move_smary()`, `move_smarz()`
- `move_zpth()`, `move_zpz1()`
- Related ZP motion methods

**New file:** `src/hxn-gui/controllers/zp_stage_controller.py`
**Integration:** Use as mixin or composition pattern

**Verification:**
- Test ZP stage movements in offline mode
- Verify button connections work
- Check error handling

---

### Step 1.2: Extract MLL Stage Controller
**Target:** ~150 lines
**Methods to extract:**
- `connect_mll_stages()`
- `move_dsx()`, `move_dsy()`, `move_dsz()`
- `move_dsth()`, `move_sbz()`
- `mll_osa_IN()`, `mll_osa_OUT()`
- Related MLL motion methods

**New file:** `src/hxn-gui/controllers/mll_stage_controller.py`

**Verification:**
- Test MLL stage movements in offline mode
- Verify OSA movements
- Check safety checks

---

## Phase 2: Extract Detector/Camera Management

### Step 2.1: Extract Detector Controller
**Target:** ~300 lines
**Methods to extract:**
- `connect_detectors_and_cameras()`
- `merlinIN()`, `merlinOUT()`, `eigerIN()`
- `vortexIN()`, `vortexOUT()`
- `cam6IN()`, `cam6OUT()`, `cam11IN()`
- `dexela_motion()`
- Detector position methods

**New file:** `src/hxn-gui/controllers/detector_controller.py`

**Verification:**
- Test detector movements in offline mode
- Verify camera controls
- Check browser integration for detector pages

---

## Phase 3: Extract Scan Management

### Step 3.1: Extract Flyscan Controller
**Target:** ~400 lines
**Methods to extract:**
- `connect_flyscan_signals()`
- `run_fly_scan()`
- `getScanValues()`, `initParams()`
- `send_to_queue()`, `send_mosaic_to_queue()`
- `copyScanPlan()`, `copyForBatch()`
- Scan parameter methods

**New file:** `src/hxn-gui/controllers/flyscan_controller.py`

**Verification:**
- Test scan parameter calculations
- Verify queue submission works
- Check scan plan copy functionality

---

## Phase 4: Extract Energy & Alignment

### Step 4.1: Extract Energy Controller
**Target:** ~200 lines
**Methods to extract:**
- `connect_energy_change()`
- `change_energy()`, `update_energy_calc()`
- `move_energy_with_sid_gui()`
- Energy-related helper methods

**New file:** `src/hxn-gui/controllers/energy_controller.py`

**Verification:**
- Test energy calculations
- Verify mirror position updates
- Check harmonic calculations

---

### Step 4.2: Extract Alignment Tools
**Target:** ~250 lines
**Methods to extract:**
- `connect_alignment_tools()`
- `zpFocusScan()`, `mll_focus_scan()`
- `mll_rot_alignment_()`, `zp_rot_alignment_()`
- `zp_to_cam11_view_()`, `zp_to_nanobeam_()`
- SSA2, S5 slit methods

**New file:** `src/hxn-gui/controllers/alignment_controller.py`

**Verification:**
- Test focus scan calculations
- Verify alignment tool connections
- Check rotation alignment logic

---

## Phase 5: Extract UI & Setup Components

### Step 5.1: Extract User Setup Manager
**Target:** ~300 lines
**Methods to extract:**
- `connect_user_setup_signals()`
- `new_user_setup()`, `fill_user_info()`
- `import_xrf_elem_list()`, `export_xrf_elem_list()`
- `populate_elems_from_combobox()`
- XRF element management

**New file:** `src/hxn-gui/managers/user_setup_manager.py`

**Verification:**
- Test XRF element list import/export
- Verify user info auto-fill
- Check proposal integration

---

### Step 5.2: Extract Plotting Manager
**Target:** ~150 lines
**Methods to extract:**
- `connect_plotting_controls()`
- `plot_me()`, `plot_erf_fit()`, `plot_line_center()`
- `close_all_plots()`, `load_last_scan_to_plot()`

**New file:** `src/hxn-gui/managers/plotting_manager.py`

**Verification:**
- Test plot generation (may need mock data)
- Verify element selection
- Check plot closing

---

### Step 5.3: Extract Sample Position Manager
**Target:** ~300 lines
**Methods to extract:**
- `connect_sample_pos_widgets()`
- `get_current_position()`, `copy_current_pos()`
- `print_roi_position()`
- Sample position management methods

**New file:** `src/hxn-gui/managers/sample_position_manager.py`

**Verification:**
- Test position storage/retrieval
- Verify ROI position handling
- Check copy functionality

---

## Phase 6: Extract Thread Management

### Step 6.1: Move Thread Classes to Separate Module
**Target:** ~200 lines
**Classes to extract:**
- `liveStatus(QThread)`
- `liveUpdate(QThread)`
- `liveThresholdUpdate(QThread)`
- `updateScanProgress(QThread)`
- `WorkerThread(QThread)`

**New file:** `src/hxn-gui/threads/background_threads.py`

**Verification:**
- Test thread creation
- Verify signal/slot connections
- Check thread cleanup

---

### Step 6.2: Extract Thread Management Methods
**Target:** ~100 lines
**Methods to extract:**
- `liveUpdateThread()`, `scanStatusThread()`
- `pump_update_thread()`, `flytube_pressure_status()`
- `create_live_pv_dict()`, `create_pump_pv_dict()`
- `handle_value_signals()`, `handle_bool_signals()`

**New file:** `src/hxn-gui/managers/thread_manager.py`

**Verification:**
- Test PV monitoring (if online)
- Verify thread start/stop
- Check signal handling

---

## Phase 7: Extract Sample Exchange & Miscellaneous

### Step 7.1: Extract Sample Exchange Controller
**Target:** ~200 lines
**Methods to extract:**
- `connect_sample_exchange()`
- Sample chamber operation methods
- Vacuum-related methods

**New file:** `src/hxn-gui/controllers/sample_exchange_controller.py`

**Verification:**
- Test sample exchange logic
- Verify safety checks
- Check vacuum monitoring

---

### Step 7.2: Extract Utility & Helper Methods
**Target:** ~100 lines
**Methods to extract:**
- `moveAMotor()`, `move_motor_with_pv()`
- `runTask()`, `onTaskFinished()`
- `set_input_validators()`
- Various helper methods

**New file:** `src/hxn-gui/utils/motion_helpers.py`

**Verification:**
- Test motor movement helpers
- Verify validator setup
- Check task execution

---

## Implementation Pattern

For each refactoring step:

```python
# Pattern 1: Mixin Class (for closely coupled UI components)
class ZPStageController:
    """Handles ZP stage movements and controls"""
    
    def connect_zp_stages(self):
        """Connect ZP stage UI signals"""
        ...
    
    def move_smarx(self, neg_=False):
        """Move SMAR-X stage"""
        ...

# In main file:
class Ui(QtWidgets.QMainWindow, Ui_window, ZPStageController, MLLStageController, ...):
    ...

# Pattern 2: Composition (for loosely coupled components)
class DetectorController:
    """Manages detector positions and states"""
    
    def __init__(self, parent_ui):
        self.ui = parent_ui
        self.client = parent_ui.client
        ...

# In main file:
class Ui(QtWidgets.QMainWindow, Ui_window):
    def __init__(self):
        ...
        self.detector_ctrl = DetectorController(self)
        ...
```

---

## Testing Strategy

After each refactoring step:

1. **Import Check:** Verify the GUI loads without errors
2. **UI Elements:** Check that buttons/widgets are still connected
3. **Method Calls:** Test key functionality in offline mode
4. **Error Handling:** Verify error decorators still work
5. **Git Commit:** Commit with descriptive message

---

## Benefits After Completion

- **Main file:** ~500-800 lines (down from 3,075)
- **Modules:** 12-15 focused, testable modules
- **Maintainability:** Each module handles one concern
- **Testing:** Easier to write unit tests for each module
- **Documentation:** Clearer code organization
- **Team:** Multiple developers can work on different modules

---

## Current Status

- [x] Created git branch: `refactor/modularize-gui`
- [x] Committed baseline: Thread settings dialog removal
- [x] **COMPLETED:** Phase 1, Step 1.1 - Extract ZP Stage Controller (✓ 71 lines extracted)
- [ ] **NEXT:** Test Step 1.1 in offline mode
- [ ] **THEN:** Phase 1, Step 1.2 - Extract MLL Stage Controller

---

## Notes

- Keep all decorators (`@show_error_message_box`, `@with_motion_feedback`)
- Maintain signal/slot connections
- Preserve all error handling
- Keep comments and TODOs
- Update imports as needed
