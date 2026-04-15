# HXN GUI Refactoring Status

## ✅ Completed Components

### 1. Package Structure
- [x] Created modular directory structure
- [x] Set up proper package hierarchy
- [x] Created all `__init__.py` files with documentation

### 2. Configuration Module (`config/`)
- [x] `constants.py` - Centralized all hardcoded values
  - File paths and directories
  - Detector configurations (motion & data names)
  - Default positions (Vortex, FS_FDET, Dexela, SSA2, S5, MLL OSA)
  - Vacuum pressure thresholds
  - Scan parameter presets (20x20, 30x30, 6x6, 2x2)
  - Scan constraints and limits
  - EPICS PV addresses (motors, detectors, vacuum, shutters)
  - Web URLs  
  - Thread update intervals
  - Motor and detector dictionaries
  - Validation patterns
  
- [x] `settings.py` - User-configurable settings
  - Settings persistence (JSON in ~/.hxn_gui/)
  - Default settings dictionary
  - Settings manager class with get/set/reset
  - Secure credential management (environment variables)
  - Settings validation
  - Fixed security issue (removed hardcoded token)

### 3. Workers Module (`workers/`)
- [x] `live_updates.py` - PV monitoring threads
  - `LiveStatusThread` (replaces `liveStatus`)
  - `LiveUpdateThread` (replaces `liveUpdate`)
  - `LiveThresholdUpdateThread` (replaces `liveThresholdUpdate`)
  - Added stop() methods for graceful shutdown
  - Added comprehensive docstrings
  
- [x] `scan_progress.py` - Scan progress tracking
  - `ScanProgressThread` (replaces `updateScanProgress`)
  - Auto-completion detection
  - Error handling
  
- [x] `chamber_ops.py` - Chamber operation threads
  - `PumpingThread` (refactored with stop() method)
  - `VentingThread` (refactored with stop() method)
  - `HeBackfillThread` (refactored with stop() method)
  - Improved error handling
  
- [x] `monitoring.py` - General monitoring
  - `LivePressureMonitorThread` (replaces `LivePressureValueThread`)
  - `GenericWorkerThread` (replaces `WorkerThread`)

### 4. Utils Module (`utils/`)
- [x] Moved existing `utilities.py` to `utils/`
- [x] Moved existing `element_lines.py` to `utils/`
- [x] Created `__init__.py` with proper exports

### 5. Core Module (`core/`)
- [x] Moved existing `HXNSampleExchange.py` to `core/`
- [x] Moved existing `hxn_data_transfer.py` to `core/`
- [x] Created `__init__.py` with proper exports

### 6. Documentation
- [x] `README.md` - Comprehensive package overview
  - Package structure diagram
  - Key improvements
  - Migration guide overview
  - Next steps roadmap
  - Benefits explanation
  
- [x] `MIGRATION_GUIDE.md` - Step-by-step migration instructions
  - Import updates
  - Security fixes
  - Thread instantiation changes
  - Search & replace guide
  - Testing checklist
  
- [x] `REFACTORING_STATUS.md` - This file
  - Tracks completed and pending work
  - Detailed component breakdown

### 7. Main Package `__init__.py`
- [x] Version information (v4.0.0)
- [x] Subpackage imports
- [x] Convenience exports
- [x] Comprehensive docstring

---

## 🔄 Pending Components

### Phase 2: Controller Extraction (Future Work)

The main `hxn_gui_v3.py` (2,887 lines) still needs to be split into controllers:

#### `controllers/flyscan.py` (~400 lines)
- [ ] Extract flyscan control methods
- [ ] Methods: `getScanValues()`, `run_fly_scan()`, `fill_common_scan_params()`
- [ ] Methods: `copyScanPlan()`, `copyForBatch()`, `disableMot2()`, `enableMot2()`
- [ ] Methods: `progress_bar_update()`, `quit_scan()`, `requestScanPause()`, etc.

#### `controllers/stage_navigator.py` (~250 lines)
- [ ] Extract ZP stage methods: `move_smarx()`, `move_smary()`, `move_smarz()`, `move_zpth()`, `move_zpz1()`
- [ ] Extract MLL stage methods: `move_dsx()`, `move_dsy()`, `move_dsz()`, `move_dsth()`, `move_sbz()`
- [ ] Extract helpers: `moveAMotor()`, `move_motor_with_pv()`

#### `controllers/energy_manager.py` (~200 lines)
- [ ] Extract energy management methods
- [ ] Methods: `update_energy_calc()`, `change_energy()`, `change_energy_()`
- [ ] Methods: `move_energy_with_sid_gui()`, `move_to_user_input_pos()`, `move_energy_with_scan_num()`
- [ ] Fix static method issues (lines noted in analysis)

#### `controllers/detector_manager.py` (~350 lines)
- [ ] Extract detector positioning methods
- [ ] Methods: `merlinIN()`, `merlinOUT()`, `eigerIN()`, `dexela_motion()`
- [ ] Methods: `vortexIN()`, `vortexOUT()`, `cam11IN()`, `cam6IN()`, `cam6OUT()`, `cam6LASER()`
- [ ] Methods: `FS_IN()`, `FS_OUT()`, `read_dexela_ROI1()`, `reset_dexela_ROI1()`
- [ ] Methods: `calc_and_fill_pos_2angle()`, `move_diff_stage()`, `move_diff_z()`

#### `controllers/alignment_tools.py` (~350 lines)
- [ ] Extract alignment methods
- [ ] Methods: `SSA2_Pos()`, `S5_Pos()`, `ZP_OSA_OUT()`, `ZP_OSA_IN()`, `mll_osa_OUT()`, `mll_osa_IN()`
- [ ] Methods: `ZP_BS_OUT()`, `ZP_BS_IN()`, `zpFocusScan()`, `mll_focus_scan()`
- [ ] Methods: `zp_to_cam11_view_()`, `zp_to_nanobeam_()`, `mll_to_cam11_view_()`, `mll_to_nanobeam_()`
- [ ] Methods: `mll_rot_alignment_()`, `zp_rot_alignment_()`, `apply_mll_rot_algn_corr()`, `apply_zp_rot_algn_corr_()`

#### `controllers/sample_pos_manager.py` (~300 lines)
- [ ] Extract sample position methods
- [ ] Methods: `get_current_position()`, `record_sample_pos()`, `move_stage_to_roi()`
- [ ] Methods: `export_listitems_to_json()`, `import_list_items_from_json()`, `clear_list_widget_items()`
- [ ] Methods: `recover_pos_from_sid_zp()`, `recover_pos_from_sid_mll()`, `view_scan_id_pos()`
- [ ] Methods: `viewScanMetaData()`, `copy_current_pos()`, `print_roi_position()`

#### `controllers/vacuum_control.py` (~200 lines)
- [ ] Extract vacuum control UI methods (logic already in workers)
- [ ] Methods: `start_pumping_in_thread()`, `vent_in_thread()`, `he_backfill_in_thread()`
- [ ] Methods: `pumping_stop()`, `live_pressure_plot_thread()`, `pump_update_thread()`

#### `controllers/user_manager.py` (~200 lines)
- [ ] Extract user setup methods
- [ ] Methods: `fill_user_info()`, `new_user_setup()`, `existing_user_setup()`, `existing_pdf_setup()`
- [ ] Methods: `import_xrf_elem_list()`, `export_xrf_elem_list()`, `populate_elems_from_combobox()`
- [ ] Methods: `apply_xrf_elems()`, `copy_data_to_globus()`

#### `controllers/queue_manager.py` (~200 lines)
- [ ] Extract QServer integration methods
- [ ] Methods: `send_to_queue()`, `send_mosaic_to_queue()`, `toggle_manual_roi_box()`
- [ ] Methods: `fill_current_pos()`, `get_manual_roi()`

#### `controllers/plotting_tools.py` (~150 lines)
- [ ] Extract plotting methods
- [ ] Methods: `plot_me()`, `load_last_scan_to_plot()`, `plot_erf_fit()`, `plot_line_center()`
- [ ] Methods: `close_all_plots()`, `plot_pressure()`

#### `controllers/pdf_logger.py` (~50 lines)
- [ ] Extract PDF logging methods
- [ ] Methods: `select_pdf_wd()`, `select_pdf_image()`, `generate_pdf()`, `force_save_pdf()`
- [ ] Methods: `InsertFigToPDF()`

### Phase 3: Main GUI Refactoring

#### `gui/main_window.py`
- [ ] Extract main `Ui` class from `hxn_gui_v3.py`
- [ ] Compose controllers as mixins or components
- [ ] Keep only:
  - `__init__()` - initialization & controller setup
  - Signal/slot connections (delegate to controllers)
  - UI event handlers (delegate to controllers)
  - Application lifecycle (`closeEvent()`, `close_application()`, `reload_gui()`)
- [ ] Target: ~600-800 lines (down from 2,887)

#### `gui/dialogs.py`
- [ ] Extract any custom dialog classes
- [ ] Create reusable dialog components

### Phase 4: Testing & Validation

- [ ] Unit tests for workers
- [ ] Unit tests for controllers
- [ ] Integration tests for main GUI
- [ ] End-to-end tests for critical workflows
- [ ] Performance benchmarks

### Phase 5: Final Cleanup

- [ ] Update `hxn_gui_v3.py` to use new imports
- [ ] Remove old thread class definitions from `hxn_gui_v3.py`
- [ ] Validate all functionality
- [ ] Update deployment scripts
- [ ] Archive old versions to `Archieved/`

---

## 📊 Progress Summary

### Lines of Code Reduction
- **Before:** 2,887 lines in `hxn_gui_v3.py`
- **Extracted so far:** ~600 lines (workers)
- **Remaining to extract:** ~1,700 lines (controllers)
- **Target main file:** ~600 lines (orchestration only)

### Files Created
- **Config:** 3 files (constants, settings, __init__)
- **Workers:** 5 files (4 modules + __init__)
- **Utils:** 1 file (__init__, modules already existed)
- **Core:** 1 file (__init__, modules already existed)
- **Controllers:** 1 file (__init__, stub)
- **GUI:** 1 file (__init__, stub)
- **Documentation:** 4 files (README, MIGRATION_GUIDE, REFACTORING_STATUS, main __init__)
- **Total new files:** 16

### Security Improvements
- ✅ Removed hardcoded credentials
- ✅ Added environment variable support
- ✅ Created secure credential management system

### Code Quality Improvements
- ✅ Added comprehensive docstrings to all workers
- ✅ Added type hints where appropriate
- ✅ Improved error handling in threads
- ✅ Added graceful shutdown mechanisms (stop() methods)
- ✅ Removed duplicate imports
- ✅ Centralized configuration

---

## 🎯 Immediate Next Steps

1. **Test the refactored workers:**
   - Import workers in a test script
   - Verify all signals/slots work
   - Check for any missing dependencies

2. **Apply migration to hxn_gui_v3.py:**
   - Update imports to use new worker classes
   - Remove old thread class definitions
   - Test that GUI still works

3. **Begin controller extraction:**
   - Start with `flyscan.py` (most self-contained)
   - Extract methods maintaining backwards compatibility
   - Test each controller independently

4. **Documentation:**
   - Add API documentation
   - Create usage examples
   - Document common patterns

---

## 📝 Notes

- All original functionality preserved
- Backwards compatibility maintained where possible
- No breaking changes to external interfaces yet
- Workers can be used independently of main GUI
- Configuration can be managed programmatically
- Settings persist across sessions

## 🔗 Related Files

- `/README.md` - Package overview and structure
- `/MIGRATION_GUIDE.md` - Step-by-step migration instructions
- `/hxn_gui_v3.py` - Original monolithic file (to be refactored)
- `/config/` - All configuration modules
- `/workers/` - All background thread workers

---

**Last Updated:** April 15, 2026  
**Status:** Phase 1 Complete ✅ | Phase 2-5 Pending 🔄
