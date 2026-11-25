"""USWDS look shared by the ROI Planner and the QServer tab (palette + stylesheet)."""
from qtpy import QtGui

USWDS_INK = "#1b1b1b"
USWDS_BASE_LIGHTEST = "#f0f0f0"
USWDS_BASE_LIGHTER = "#dfe1e2"
USWDS_BASE_LIGHT = "#a9aeb1"
USWDS_BASE = "#71767a"
USWDS_BASE_DARK = "#565c65"
USWDS_BASE_DARKER = "#3d4551"
USWDS_PRIMARY = "#005ea2"
USWDS_PRIMARY_VIVID = "#0050d8"
USWDS_PRIMARY_DARK = "#1a4480"
USWDS_SECONDARY = "#d83933"
USWDS_ACCENT_COOL = "#00bde3"
USWDS_ACCENT_COOL_DARK = "#28a0cb"
USWDS_WARNING = "#ffbe2e"
USWDS_SUCCESS = "#00a91c"
USWDS_ERROR = "#d54309"


def apply_uswds_theme(widget) -> None:
    """Give widget and all its children the USWDS colours, fonts and button style.

    Args:
        widget: any QWidget (a tab page, a window, ...).

    Example:
        apply_uswds_theme(gui.tab_qserver_console)
    """
    widget.setAutoFillBackground(True)
    palette = widget.palette()
    palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(USWDS_BASE_LIGHTEST))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor(USWDS_INK))
    palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor("#ffffff"))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(USWDS_BASE_LIGHTEST))
    palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor(USWDS_INK))
    palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(USWDS_BASE_LIGHTEST))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor(USWDS_INK))
    palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(USWDS_PRIMARY))
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText, QtGui.QColor("#ffffff"))
    palette.setColor(QtGui.QPalette.ColorRole.Link, QtGui.QColor(USWDS_PRIMARY_VIVID))
    widget.setPalette(palette)

    widget.setStyleSheet(
        f"""
        QMainWindow, QWidget {{
            background-color: {USWDS_BASE_LIGHTEST};
            color: {USWDS_INK};
            font-size: 11px;
        }}
        QGroupBox {{
            background-color: #ffffff;
            border: 1px solid {USWDS_BASE_LIGHTER};
            border-radius: 8px;
            margin-top: 10px;
            padding: 12px 10px 10px 10px;
            font-weight: 600;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 6px;
            color: {USWDS_PRIMARY_DARK};
            background-color: #ffffff;
        }}
        QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox, QTextEdit, QPlainTextEdit, QTableWidget, QTableView, QListWidget, QTabWidget::pane {{
            background-color: #ffffff;
            border: 1px solid {USWDS_BASE_LIGHT};
            border-radius: 6px;
            color: {USWDS_INK};
        }}
        QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {{
            min-height: 26px;
            padding: 3px 7px;
        }}
        QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus, QTextEdit:focus {{
            border: 2px solid {USWDS_PRIMARY_VIVID};
        }}
        QPushButton {{
            background-color: {USWDS_PRIMARY};
            color: #ffffff;
            border: 1px solid {USWDS_PRIMARY_DARK};
            border-radius: 6px;
            min-height: 28px;
            padding: 4px 10px;
            font-weight: 600;
        }}
        QPushButton:hover {{
            background-color: {USWDS_PRIMARY_VIVID};
        }}
        QPushButton:pressed {{
            background-color: {USWDS_PRIMARY_DARK};
        }}
        QPushButton:disabled {{
            background-color: {USWDS_BASE_LIGHT};
            border-color: {USWDS_BASE};
            color: #ffffff;
        }}
        QTabBar::tab {{
            background-color: {USWDS_BASE_LIGHTER};
            color: {USWDS_BASE_DARKER};
            border: 1px solid {USWDS_BASE_LIGHT};
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            padding: 6px 10px;
            margin-right: 4px;
        }}
        QTabBar::tab:selected {{
            background-color: #ffffff;
            color: {USWDS_PRIMARY_DARK};
        }}
        QHeaderView::section {{
            background-color: {USWDS_PRIMARY_DARK};
            color: #ffffff;
            padding: 5px;
            border: none;
            font-weight: 600;
        }}
        QTableWidget, QTableView {{
            gridline-color: {USWDS_BASE_LIGHTER};
            selection-background-color: {USWDS_ACCENT_COOL};
            selection-color: {USWDS_INK};
        }}
        QTableWidget::item {{
            padding: 4px;
        }}
        QRadioButton, QCheckBox {{
            spacing: 8px;
        }}
        QStatusBar {{
            background-color: {USWDS_BASE_DARKER};
            color: #ffffff;
        }}
        QLabel {{
            color: {USWDS_BASE_DARKER};
        }}
        """
    )

