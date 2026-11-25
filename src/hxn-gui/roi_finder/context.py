"""Connections and beamline settings for roi_finder, supplied by the host application.

The HXN GUI calls configure(...) with its own databroker, QServer API and microscope settings, so
roi_finder neither opens a second databroker nor creates a second REManagerAPI. Run standalone,
the getters fall back to creating them on first use.
"""
_db = None
_rm = None
_scan_motors = None  # callable -> (fast motor, slow motor, zp_flag)
_max_points = None  # callable -> int


def configure(db=None, rm=None, scan_motors=None, max_points=None):
    global _db, _rm, _scan_motors, _max_points
    _db, _rm, _scan_motors, _max_points = db, rm, scan_motors, max_points


def get_db():
    global _db
    if _db is None:
        from hxntools.CompositeBroker import db
        _db = db
    return _db


def get_rm():
    global _rm
    if _rm is None:
        from bluesky_queueserver_api.zmq import REManagerAPI
        _rm = REManagerAPI()
    return _rm


def scan_motors():
    """(fast motor, slow motor, zp_flag) for fine scans; ZP fine stages when no host is attached."""
    return _scan_motors() if _scan_motors else ("zpssx", "zpssy", True)


def max_points(default):
    return int(_max_points()) if _max_points else default
