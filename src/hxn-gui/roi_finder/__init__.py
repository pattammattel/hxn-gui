"""XRF ROI scan planner, embedded in the HXN GUI as the "ROI Planner" tab.

Copied from the roi_finder project (github: pattammattel/roi_finder, commit c3776df) and adapted:
qtpy instead of PyQt6, relative imports, and connections/microscope settings supplied through
context.configure() instead of module-level databroker and REManagerAPI instances.
Standalone: `python -m roi_finder.main` from src/hxn-gui.
"""
