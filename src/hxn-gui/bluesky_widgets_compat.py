"""Fixes for bluesky-widgets 0.0.18 under PyQt6 and bluesky-queueserver-api 0.0.14; import before building its widgets.

1. It calls QCheckBox.setChecked(Qt.Checked), which PyQt6 rejects (it needs a bool).
2. Its stateChanged handlers test `state == Qt.Checked`; PyQt6 passes an int, so the test is always
   False and the "Auto" queue start, "All Parameters" and console autoscroll checkboxes do nothing.
3. Its status update catches client.RequestError / client.ClientError, which bluesky-queueserver-api
   0.0.14 names HTTPRequestError / HTTPClientError; without aliases every timeout raises AttributeError
   and the status never shows OFFLINE.
Only bluesky-widgets' module and classes (and the two alias names on REManagerAPI) are patched.
Remove once bluesky-widgets supports PyQt6.
"""
import functools

from qtpy import QtWidgets
from qtpy.QtCore import Qt

import bluesky_widgets.qt.run_engine_client as rec

_HANDLERS = (
    (rec.QtReQueueControls, "_cb_queue_autostart_state_changed"),
    (rec._QtReViewer, "_cb_show_optional_state_changed"),
    (rec.QtReConsoleMonitor, "_cb_pause_autoscroll_state_changed"),
)


class _CheckBox(QtWidgets.QCheckBox):
    def setChecked(self, checked):
        if isinstance(checked, Qt.CheckState):
            checked = checked == Qt.CheckState.Checked
        super().setChecked(bool(checked))


def _as_check_state(method):
    @functools.wraps(method)
    def wrapper(self, state, *args, **kwargs):
        if isinstance(state, int) and not isinstance(state, Qt.CheckState):
            state = Qt.CheckState(state)
        return method(self, state, *args, **kwargs)
    return wrapper


def apply():
    if getattr(rec, "_hxn_pyqt6_compat", False):
        return
    from bluesky_queueserver_api.zmq import REManagerAPI
    for old, new in (("RequestError", "HTTPRequestError"), ("ClientError", "HTTPClientError")):
        if not hasattr(REManagerAPI, old) and hasattr(REManagerAPI, new):
            setattr(REManagerAPI, old, getattr(REManagerAPI, new))
    rec.QCheckBox = _CheckBox
    for cls, name in _HANDLERS:
        setattr(cls, name, _as_check_state(getattr(cls, name)))
    rec._hxn_pyqt6_compat = True


apply()
