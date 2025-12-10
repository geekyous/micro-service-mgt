from PySide6.QtWidgets import QApplication

from ui.windows.main_window import MainWindow


class MicroServiveApp:
    def __init__(self):
        self.app = QApplication([])
        self.window = MainWindow()

    def run(self):
        self.window.show()
        self.app.exec()
