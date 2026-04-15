"""
HXN GUI Package

A modular PyQt5-based graphical user interface for the Hard X-ray Nanoprobe (HXN)
beamline at NSLS-II.

Author: Ajith Pattammattel
Original Date: 2020-06-23
Last Major Update: 2024-03-07
Refactored: 2026-04-15

Package Structure:
    config/         - Configuration constants and settings
    workers/        - Background thread workers (QThread)
    controllers/    - Domain-specific controller modules (planned)
    gui/            - Main GUI components (planned)
    utils/          - Utility functions and helpers
    core/           - Core beamline functionality

Usage:
    # Import the main GUI (legacy, from original file)
    from hxn_gui.hxn_gui_v3 import Ui
    
    # Import workers
    from hxn_gui.workers import LiveUpdateThread, PumpingThread
    
    # Import configuration
    from hxn_gui.config import constants, settings
    
    # Import utilities
    from hxn_gui.utils import utilities, element_lines
    
    # Import core modules
    from hxn_gui.core import SampleExchangeProtocol

Version History:
    v3.0 (2024-03-07): Latest monolithic version
    v4.0 (2026-04-15): Refactored modular architecture
        - Extracted worker threads to separate package
        - Centralized configuration constants
        - Added secure credential management
        - Improved package organization
"""

__version__ = '4.0.0'
__author__ = 'Ajith Pattammattel'

# Subpackages
from . import config
from . import workers
from . import utils
from . import core
from . import controllers
from . import gui

# Convenience imports - commonly used items
from .config.settings import settings
from .core import SampleExchangeProtocol

__all__ = [
    # Version info
    '__version__',
    '__author__',
    # Subpackages
    'config',
    'workers',
    'utils',
    'core',
    'controllers',
    'gui',
    # Convenience exports
    'settings',
    'SampleExchangeProtocol',
]
