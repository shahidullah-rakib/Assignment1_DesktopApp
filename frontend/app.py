import sys
import os
import threading
from PyQt5 import QtWidgets

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main_window import MainWindow
from backend.mouse_tracker import MouseTracker

def run_mouse_tracker(ui_update_callback):
    mouse_tracker = MouseTracker(ui_update_callback)
    mouse_tracker.start_listener()

class App:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()
        self.start_mouse_tracking()

    def start_mouse_tracking(self):
        mouse_thread = threading.Thread(
            target=run_mouse_tracker, 
            args=(self.window.display_click_event,)
        )
        mouse_thread.daemon = True
        mouse_thread.start()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app_instance = App()
    app_instance.run()
