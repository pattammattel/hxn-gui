"""
Simple GUI for testing QtPy environment compatibility.
Tests that QtPy works with available Qt bindings (PySide6, PyQt6, etc.)

Usage:
    Standalone: python simple_gui_for_testing.py
    IPython: %gui qt
             run -i simple_gui_for_testing.py
"""

import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from qtpy.QtCore import Qt


class SimpleTestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.click_count = 0
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        # Set window properties
        self.setWindowTitle('QtPy Environment Test')
        self.setGeometry(100, 100, 400, 200)
        
        # Create layout
        layout = QVBoxLayout()
        
        # Create label
        self.label = QLabel('Click the button below!', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; padding: 20px;")
        
        # Create button
        self.button = QPushButton('Click Me!', self)
        self.button.setStyleSheet("font-size: 14px; padding: 10px;")
        self.button.clicked.connect(self.on_button_clicked)
        
        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        # Set the layout
        self.setLayout(layout)
        
        # Show which Qt binding is being used
        self.check_qt_binding()
    
    def on_button_clicked(self):
        """Handle button click event."""
        self.click_count += 1
        self.label.setText(f'Button clicked {self.click_count} time(s)! ✓')
        print(f"Button clicked: {self.click_count}")
    
    def check_qt_binding(self):
        """Display which Qt binding QtPy is using."""
        try:
            import qtpy
            qt_api = qtpy.API_NAME
            print(f"QtPy is using: {qt_api}")
            self.setWindowTitle(f'QtPy Test - Using {qt_api}')
        except Exception as e:
            print(f"Could not determine Qt binding: {e}")


if __name__ == "__main__":
    # Create QApplication
    app = QApplication(sys.argv)
    
    # Create and show window
    window = SimpleTestWindow()
    window.show()
    
    print("\n" + "="*50)
    print("GUI Test Window Launched")
    print("="*50)
    
    # Start event loop
    sys.exit(app.exec())
