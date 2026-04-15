# How to Run HXN GUI

## Quick Answer

You have **multiple options** that all work:

## Option 1: Original Method (Still Works!) ✅

```bash
cd /Users/ajithpattammattel/Desktop/8-Codes/hxn-gui/src/hxn-gui
ipython hxn_gui_v3.py
```

This still works because `hxn_gui_v3.py` hasn't been modified yet.

## Option 2: New Launcher Script (Recommended) ⭐

```bash
cd /Users/ajithpattammattel/Desktop/8-Codes/hxn-gui/src/hxn-gui

# Standard Python
python run_gui.py

# IPython (your preferred way)
ipython run_gui.py

# IPython interactive mode (keeps console open)
ipython -i run_gui.py
```

## Option 3: Run as Python Package

```bash
cd /Users/ajithpattammattel/Desktop/8-Codes/hxn-gui/src

# Standard Python
python -m hxn-gui

# IPython
ipython -m hxn-gui
```

## Option 4: Direct Import (for development/testing)

```bash
cd /Users/ajithpattammattel/Desktop/8-Codes/hxn-gui/src/hxn-gui
ipython
```

Then in IPython:
```python
from hxn_gui_v3 import Ui
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = Ui()
window.show()
app.exec_()
```

## Option 5: After Full Migration (Future)

Once `hxn_gui_v3.py` is fully migrated to use the new structure:

```python
from hxn_gui.gui.main_window import MainWindow  # Future
from hxn_gui import run_application  # Future
```

---

## What Changed?

### Structure Before:
```
hxn-gui/
└── hxn_gui_v3.py  (one monolithic file)
```

### Structure After:
```
hxn-gui/
├── run_gui.py          ← NEW: Simple launcher script
├── __main__.py         ← NEW: Package entry point
├── hxn_gui_v3.py       ← UNCHANGED: Still works!
├── config/             ← NEW: Configuration
├── workers/            ← NEW: Background threads
├── utils/              ← REORGANIZED
└── core/               ← REORGANIZED
```

### What Still Works:
- ✅ `ipython hxn_gui_v3.py` (your original command)
- ✅ All existing functionality
- ✅ Import paths (legacy modules still in place)

### What's New:
- ✅ `run_gui.py` - Convenient launcher
- ✅ `__main__.py` - Package-style execution
- ✅ Better organization for future development
- ✅ No breaking changes!

---

## Environment Setup (Important!)

Since credentials were removed from source code, set environment variables:

```bash
# Add to your ~/.zshrc or ~/.bashrc
export HXN_GITHUB_TOKEN="your_token_here"

# Or set temporarily for one session
export HXN_GITHUB_TOKEN="your_token_here"
ipython run_gui.py
```

---

## Troubleshooting

### If you get import errors:

**Problem:** Can't import workers
```python
ImportError: No module named 'hxn_gui.workers'
```

**Solution:** Make sure you're in the correct directory:
```bash
cd /Users/ajithpattammattel/Desktop/8-Codes/hxn-gui/src/hxn-gui
```

### If you get Qt errors:

**Problem:** Display/X11 errors

**Solution:** Same as before - ensure your display is properly configured

---

## Development Workflow

### For Normal Use:
```bash
ipython run_gui.py
```

### For Development/Debugging:
```bash
ipython -i run_gui.py  # Keeps console open after GUI starts
```

### For Testing New Workers:
```python
from hxn_gui.workers import LiveUpdateThread
thread = LiveUpdateThread(pv_dict, 500)
# Test your worker...
```

### For Testing Configuration:
```python
from hxn_gui.config import constants
from hxn_gui.config.settings import settings

print(constants.MAX_SCAN_POINTS)
print(settings.get('microscope_mode'))
```

---

## Summary

**Short answer:** Your original command `ipython hxn_gui_v3.py` still works!

**Better option:** Use `ipython run_gui.py` - it's cleaner and forward-compatible

**Best practice:** Eventually transition to the refactored structure once `hxn_gui_v3.py` is updated (see MIGRATION_GUIDE.md)

---

## Next Steps

1. **Now:** Keep using `ipython hxn_gui_v3.py` (or try `ipython run_gui.py`)
2. **Soon:** Update imports in `hxn_gui_v3.py` to use new workers
3. **Later:** Migrate to fully modular structure with controllers

No rush - everything still works as before! The refactoring is backward-compatible.
