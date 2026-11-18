"""
Candidate helpers for the HXN GUI, kept here for testing before being moved into hxn_gui_v3.py.

jog_motor: relative motor jog through ophyd (no RunEngine, so it also works during a scan).
- Non-blocking: motor.move(target, wait=False) returns immediately; the GUI stays responsive.
- Soft limits are checked before moving (LimitError -> warning box).
- A status callback reports success or failure in the status bar.
- The step is added to the setpoint, not the readback, so quick repeated clicks add up.

Example use inside Ui.__init__ (motors come from the bsui session):

    from scripts_to_test import MotionNotifier, jog_motor

    self.motion_notifier = MotionNotifier()
    self.motion_notifier.message.connect(self.statusbar.showMessage)
    for axis, motor in (("osax", mllosa.osax), ("osay", mllosa.osay),
                        ("bsx", mllbs.bsx), ("bsy", mllbs.bsy)):
        box = getattr(self, f"db_move_mll_{axis}")
        getattr(self, f"pb_mll_{axis}_pos").clicked.connect(
            lambda _=False, m=motor, b=box: jog_motor(self, m, b, self.motion_notifier))
        getattr(self, f"pb_mll_{axis}_neg").clicked.connect(
            lambda _=False, m=motor, b=box: jog_motor(self, m, b, self.motion_notifier, neg=True))
"""

from ophyd.utils import LimitError
from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QMessageBox


class MotionNotifier(QObject):
    # Ophyd runs status callbacks on its own thread; this signal hands the text to the GUI thread.
    message = Signal(str)


def jog_motor(gui, motor, step_box, notifier, neg=False):
    """Move `motor` by +/- step_box.value() relative to its current setpoint.

    gui: the main window (needs .statusbar); notifier: a MotionNotifier connected to the status bar.
    """
    step = -step_box.value() if neg else step_box.value()
    target = motor.user_setpoint.get() + step
    try:
        status = motor.move(target, wait=False)
    except LimitError as exc:
        QMessageBox.warning(gui, "Move refused", f"{motor.name}: {exc}")
        return None
    gui.statusbar.showMessage(f"{motor.name} moving to {target:.3f}")

    def finished(st):
        if st.success:
            notifier.message.emit(f"{motor.name} reached {motor.position:.3f}")
        else:
            notifier.message.emit(f"{motor.name} move FAILED (stalled, stopped or limit switch)")

    status.add_callback(finished)
    return status
