from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Click Tracker")
        self.setGeometry(200, 200, 400, 300)

        # Text area to display mouse click events
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.setCentralWidget(self.text_area)

    def display_click_event(self, event_text):
        """Display mouse click events in the text area."""
        self.text_area.append(event_text)
