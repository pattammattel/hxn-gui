"""Adds the roi_finder XRF ROI scan planner to the HXN GUI as a tab."""
from qtpy import QtWidgets
from qtpy.QtCore import Qt


def add_roi_planner_tab(gui, db=None, rm=None, title="ROI Planner", after="tab_advanced_scans"):
    """Build the planner and insert it after the `after` tab of gui.HXN_GUI_tabs.

    Motors and point limit follow gui.microscope_profiles, so plans use the active microscope's
    fine stages (and zp_flag) at the moment they are sent. Returns the planner widget, or None if it
    could not be created (the rest of the GUI keeps working).
    """
    try:
        from roi_finder import context
        from roi_finder.main import ROIScanPlanner
    except Exception as exc:
        print(f"  ROI Planner tab not added: {type(exc).__name__}: {exc}")
        return None

    def scan_motors():
        profiles = gui.microscope_profiles
        active = profiles["active"]
        fast, slow = profiles[active]["fly_motors"][:2]
        return fast, slow, active == "ZP"

    context.configure(db=db, rm=rm, scan_motors=scan_motors,
                      max_points=lambda: gui.microscope_profiles["flyscan_max_points"])
    planner = ROIScanPlanner()
    planner.setObjectName("roi_planner")
    planner.setWindowFlags(Qt.Widget)  # QMainWindow embedded as a page, keeping its own status bar

    page = QtWidgets.QWidget()
    page.setObjectName("tab_roi_planner")
    layout = QtWidgets.QVBoxLayout(page)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(planner)
    tabs = gui.HXN_GUI_tabs
    anchor = gui.findChild(QtWidgets.QWidget, after)
    index = tabs.indexOf(anchor) + 1 if anchor is not None else tabs.count()
    tabs.insertTab(index, page, title)
    return planner
