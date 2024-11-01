import sys
import json
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

from mouse_tracker import start_mouse_tracking
from keyboard_tracker import start_keyboard_tracking
from app_tracker import start_app_tracking
from url_tracker import start_url_monitoring

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Activity Tracker")
        self.setGeometry(100, 100, 600, 400)
        
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)

        self.start_tracking()

    def start_tracking(self):
        # Start all trackers
        start_mouse_tracking(self.log_data)
        start_keyboard_tracking(self.log_data)
        start_app_tracking(self.log_data)
        start_url_monitoring(self.log_data)

    def log_data(self, data):
        self.text_edit.append(data)

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
