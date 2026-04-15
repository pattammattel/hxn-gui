"""
HXN GUI Configuration Package

This package contains all configuration constants, settings, and credential management.

Usage:
    from hxn_gui.config import constants, settings
    from hxn_gui.config.constants import MAX_SCAN_POINTS
    from hxn_gui.config.settings import settings
"""

from . import constants
from . import settings

__all__ = ['constants', 'settings']
