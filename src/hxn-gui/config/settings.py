"""
HXN GUI Settings and Configuration

This module manages user-configurable settings and secure credential handling.
Settings can be overridden through environment variables or a configuration file.

Author: Ajith Pattammattel
Refactored: 2026-04-15
"""

import os
import json
from pathlib import Path

# =============================================================================
# Settings File Location
# =============================================================================

# Default settings file location (user's home directory)
HOME_DIR = Path.home()
SETTINGS_DIR = HOME_DIR / '.hxn_gui'
SETTINGS_FILE = SETTINGS_DIR / 'settings.json'

# Create settings directory if it doesn't exist
SETTINGS_DIR.mkdir(exist_ok=True)


# =============================================================================
# Default Settings
# =============================================================================

DEFAULT_SETTINGS = {
    'microscope_mode': 'zp',  # 'zp' or 'mll'
    'default_detector': 'dets_fast',
    'auto_plot': True,
    'confirm_large_scans': True,
    'confirm_dangerous_moves': True,
    'live_update_enabled': True,
    'live_update_interval_ms': 500,
    'enable_logging': True,
    'log_level': 'INFO',
}


# =============================================================================
# Settings Manager
# =============================================================================

class Settings:
    """Manages application settings with JSON persistence."""
    
    def __init__(self):
        """Initialize settings from file or defaults."""
        self._settings = DEFAULT_SETTINGS.copy()
        self.load()
    
    def load(self):
        """Load settings from JSON file."""
        if SETTINGS_FILE.exists():
            try:
                with open(SETTINGS_FILE, 'r') as f:
                    loaded_settings = json.load(f)
                    # Only update keys that exist in defaults
                    for key in DEFAULT_SETTINGS:
                        if key in loaded_settings:
                            self._settings[key] = loaded_settings[key]
            except Exception as e:
                print(f"Error loading settings: {e}")
                print("Using default settings")
    
    def save(self):
        """Save current settings to JSON file."""
        try:
            with open(SETTINGS_FILE, 'w') as f:
                json.dump(self._settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def get(self, key, default=None):
        """Get a setting value."""
        return self._settings.get(key, default)
    
    def set(self, key, value):
        """Set a setting value."""
        self._settings[key] = value
        self.save()
    
    def reset(self):
        """Reset all settings to defaults."""
        self._settings = DEFAULT_SETTINGS.copy()
        self.save()
    
    def __getitem__(self, key):
        """Allow dict-style access."""
        return self._settings[key]
    
    def __setitem__(self, key, value):
        """Allow dict-style assignment."""
        self.set(key, value)


# Global settings instance
settings = Settings()


# =============================================================================
# Secure Credential Management
# =============================================================================

def get_github_token():
    """
    Get GitHub token from environment variable.
    
    SECURITY: Never hardcode credentials in source code!
    Set the environment variable:
        export HXN_GITHUB_TOKEN="your_token_here"
    
    Returns:
        str: GitHub token or None if not set
    """
    token = os.environ.get('HXN_GITHUB_TOKEN')
    if not token:
        print("Warning: HXN_GITHUB_TOKEN environment variable not set")
    return token


def get_beamline_credentials():
    """
    Get beamline-specific credentials from environment variables.
    
    Returns:
        dict: Dictionary of credentials
    """
    return {
        'github_token': get_github_token(),
        # Add other credentials as needed
    }


# =============================================================================
# Configuration Validation
# =============================================================================

def validate_settings():
    """Validate current settings and fix any issues."""
    valid_modes = ['zp', 'mll']
    if settings.get('microscope_mode') not in valid_modes:
        print(f"Invalid microscope_mode: {settings.get('microscope_mode')}")
        settings.set('microscope_mode', 'zp')
    
    # Validate interval ranges
    interval = settings.get('live_update_interval_ms', 500)
    if not (100 <= interval <= 5000):
        print(f"Invalid live_update_interval_ms: {interval}")
        settings.set('live_update_interval_ms', 500)
    
    return True


# Validate on module import
validate_settings()
