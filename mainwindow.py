import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
import gui
from gui import CalendarBaseDisplay, CalendarPage, CalendarTaskPage

class MainWindow(QMainWindow):
        def __init__(self, parent = None):
                super().__init__(parent)
                self.setWindowTitle("ZenCalendar 0.0.1(Gui start)")
                self.resize(1000,600)

                central_widget = QWidget()
                self.setCentralWidget(central_widget)

                self.main_layout = QHBoxLayout(central_widget)

                self.task_side = CalendarTaskPage()
                self.calendar_main = CalendarPage()

                self.main_layout.addWidget(self.calendar_main,stretch=3)
                self.main_layout.addWidget(self.task_side,stretch=1)
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

