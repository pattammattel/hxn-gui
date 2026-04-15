"""
HXN GUI Configuration Constants

This module contains all hardcoded constants, PV addresses, default positions,
and configuration values extracted from the monolithic hxn_gui_v3.py for better
maintainability and organization.

Author: Ajith Pattammattel
Refactored: 2026-04-15
"""

import os

# =============================================================================
# File Paths
# =============================================================================

# Get the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# UI files
UI_DIR = os.path.join(BASE_DIR, 'ui_files')
UI_FILE_V3 = os.path.join(UI_DIR, 'hxn_gui_v3.ui')
UI_FILE_V4 = os.path.join(UI_DIR, 'hxn_gui_v4.ui')

# Style sheets
STYLE_DIR = os.path.dirname(BASE_DIR)
STYLE_FILE = os.path.join(STYLE_DIR, 'uswds_style.qss')

# Configuration files
CONFIG_DIR = '/nsls2/data/hxn/shared/config/bluesky/profile_collection/startup'
XRF_CONFIG_FILE = os.path.join(CONFIG_DIR, 'plot_elems.json')

# Temporary files
TEMP_DIR = os.path.join(BASE_DIR, 'temp')
ROI_POSITIONS_FILE = os.path.join(TEMP_DIR, 'gui_roi_positions.json')

# Data directories
DATA_BASE_DIR = '/nsls2/data/hxn'
USER_DATA_DIR = '/data/users'

# Python environment
PYTHON_EXECUTABLE = '/nsls2/conda/envs/2023-1.0-py310-tiled/bin/ipython'
IPYTHON_PROFILE = '--profile=collection'

# =============================================================================
# Detector and Camera Configuration
# =============================================================================

DET_CAMERA_NAMES_MOTION = ['cam11', 'merlin', 'eiger']
DET_CAMERA_NAMES_DATA = ['cam11', 'merlin1', 'merlin2', 'eiger1']

# =============================================================================
# Default Detector Positions
# =============================================================================

# Vortex XRF detector
VORTEX_OUT_POSITION = -107.0
VORTEX_OUT_THRESHOLD = 25.0  # mm, detector is "out" if position > this value

# Front-end fluorescence detector
FS_FDET_INSERT_POSITION = -57.0
FS_FDET_INSERT_THRESHOLD = -50.0  # detector is "in" if position < this value

# =============================================================================
# Dexela Detector Configuration
# =============================================================================

# ROI reset values (half resolution)
DEXELA_ROI_RESET = (0, 972, 768, 768)

# =============================================================================
# Slit and Aperture Default Positions
# =============================================================================

# SSA2 (Secondary Source Aperture 2)
SSA2_OPEN = (2.1, 2.1)  # mm
SSA2_CLOSE = (0.05, 0.03)  # mm

# S5 Slits
S5_OPEN = (4.0, 4.0)  # mm
S5_CLOSE = (0.3, 0.3)  # mm

# =============================================================================
# MLL OSA Positions
# =============================================================================

MLL_OSA_IN_THRESHOLD = 10.0  # mm, safe range for IN
MLL_OSA_OUT_THRESHOLD = 50.0  # mm, safe range for OUT

# =============================================================================
# Vacuum and Pressure Settings
# =============================================================================

# Pressure thresholds (mmHg)
PRESSURE_VENTED = 765.0  # Ready for venting
PRESSURE_HE_BACKFILL = 250.0  # Helium backfill target
PRESSURE_VACUUM_TARGET = 1.2  # Final vacuum pressure
PRESSURE_FAST_PUMP_TRIGGER = 350.0  # Trigger for fast pump

# =============================================================================
# Scan Parameter Presets
# =============================================================================

# Format: (x_range_um, y_range_um, x_steps, y_steps, dwell_time_s)
SCAN_PRESETS = {
    '20x20': (20.0, 20.0, 100, 100, 0.005),  # 20 µm scan, 100 steps, 5 ms dwell
    '30x30': (28.0, 28.0, 56, 56, 0.005),    # 28 µm scan, 56 steps, 5 ms dwell
    '6x6': (6.0, 6.0, 100, 100, 0.005),      # 6 µm scan, 100 steps, 5 ms dwell
    '2x2': (2.0, 2.0, 100, 100, 0.005),      # 2 µm scan, 100 steps, 5 ms dwell
}

# =============================================================================
# Scan Constraints and Limits
# =============================================================================

# Maximum scan points
MAX_SCAN_POINTS = 64000

# Merlin detector minimum dwell time (seconds)
MERLIN_MIN_DWELL = 0.020  # 20 ms

# Scan time warning thresholds (minutes)
SCAN_1D_WARNING_TIME = 1.0  # 1 minute
SCAN_2D_WARNING_TIME = 5.0  # 5 minutes

# Scan ID age warning
SCAN_ID_AGE_WARNING = 100  # scans

# ZP Z-axis collision warning
ZP_Z_DIVERGENCE_WARNING = 1.0  # mm

# =============================================================================
# EPICS PV Addresses
# =============================================================================

# Shutters
PV_SHUTTER_PSH = 'XF:03IDB-PPS{PSh}Cmd:Opn-Cmd'
PV_SHUTTER_ZEB = 'XF:03IDC-ES{Zeb:2}:SOFT_IN:B0'

# Monochromator
PV_MONO_ENERGY = 'XF:03ID{}Energy-I'

# Motors - ZP Stages
PV_MOTORS = {
    'smarx': 'XF:03IDC-ES{ANC350:1-Ch:5}Mtr.RBV',
    'smary': 'XF:03IDC-ES{ANC350:1-Ch:6}Mtr.RBV',
    'smarz': 'XF:03IDC-ES{ANC350:2-Ch:1}Mtr.RBV',
    'zpsth': 'XF:03IDC-ES{ANC350:2-Ch:3}Mtr.RBV',
    'zpz1': 'XF:03IDC-ES{ANC350:2-Ch:2}Mtr.RBV',
    # MLL Stages
    'dsx': 'XF:03IDC-ES{ANC350:5-Ch:1}Mtr.RBV',
    'dsy': 'XF:03IDC-ES{ANC350:5-Ch:2}Mtr.RBV',
    'dsz': 'XF:03IDC-ES{ANC350:5-Ch:3}Mtr.RBV',
    'dsth': 'XF:03IDC-ES{ANC350:6-Ch:1}Mtr.RBV',
    'sbz': 'XF:03IDC-ES{ANC350:6-Ch:2}Mtr.RBV',
}

# Detectors
PV_MERLIN_PREFIX = 'XF:03IDC-ES{Merlin:'
PV_EIGER_PREFIX = 'XF:03IDC-ES{Eiger:'
PV_DEXELA_PREFIX = 'XF:03IDC-ES{Dexela:'

# Vacuum gauges
PV_VACUUM_CHAMBER = 'XF:03IDC-VA{VT:Chm-CM:1}P-I'
PV_VACUUM_ES_PREFIX = 'XF:03IDC-VA{ES:1-'

# Scaler
PV_SCALER_PREFIX = 'XF:03IDC-ES{Sclr:'

# =============================================================================
# Web URLs  
# =============================================================================

# Detector control URLs
DETECTOR_CONTROL_URL = 'http://10.66.17.43'

# =============================================================================
# Thread Update Intervals (milliseconds)
# =============================================================================

LIVE_UPDATE_INTERVAL = 500  # 0.5 seconds
PUMP_UPDATE_INTERVAL = 2000  # 2 seconds
THRESHOLD_UPDATE_INTERVAL = 60000  # 60 seconds
SCAN_PROGRESS_INTERVAL = 100  # 0.1 seconds

# =============================================================================
# Motor Dictionary Names
# =============================================================================

# Fly scan motor names (keys for combo boxes)
FLY_MOTOR_NAMES = ['zpssx', 'zpssy', 'zpssz', 'dssx', 'dssy', 'dssz']

# Detector collection names
FLY_DET_NAMES = ['dets_fast', 'dets_fast_merlin', 'dets_fast_fs']

# =============================================================================
# GUI Validation Patterns
# =============================================================================

# Regex patterns for input validation
FLOAT_PATTERN = r'^-?\d+\.?\d*$'
INT_PATTERN = r'^\d+$'
POSITIVE_FLOAT_PATTERN = r'^\d+\.?\d*$'
