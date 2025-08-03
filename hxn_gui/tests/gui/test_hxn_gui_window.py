import pytest
from PyQt6.QtWidgets import QApplication
from hxn_gui.gui.windows.hxn_gui_window import hxn_guiWindow

@pytest.fixture(scope='module')
def app():
    import sys
    app = QApplication(sys.argv)
    yield app
    app.quit()

def test_window_starts(app):
    window = hxn_guiWindow()
    assert window is not None
    assert window.isVisible() is False  # should not be visible until shown
