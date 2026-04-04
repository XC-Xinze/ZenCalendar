import sys
from PyQt6.QtWidgets import QStackedWidget, QApplication, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QWidget
import gui
from gui import CalendarBaseDisplay, CalendarPage, CalendarTaskPage
import manager
class MainWindow(QMainWindow):
        def __init__(self, parent = None):
                super().__init__(parent)
                self.setWindowTitle("ZenCalendar 0.0.1(Gui start)")
                self.resize(1000,600)
                self.manager_gui = manager.CalManager()
                self.manager_gui.load()

                central_widget = QWidget()
                self.setCentralWidget(central_widget)
                self.main_layout = QHBoxLayout(central_widget)

                # for nav - left side
                self.nav_bar = QWidget()
                nav_layout = QVBoxLayout(self.nav_bar)

                self.btn_calendar = QPushButton("Calendar View")
                self.btn_task = QPushButton("Tasks View")
                self.btn_union_view = QPushButton("Union View")
                nav_layout.addWidget(self.btn_union_view)
                nav_layout.addWidget(self.btn_calendar)
                nav_layout.addWidget(self.btn_task)
                nav_layout.addStretch()

                #main part for contents
                self.task_side = CalendarTaskPage(self.manager_gui)
                self.calendar_main = CalendarPage(self.manager_gui)

                self.main_layout.addWidget(self.nav_bar)
                self.main_layout.addWidget(self.calendar_main, stretch=4)
                self.main_layout.addWidget(self.task_side,stretch=2)

                self.btn_union_view.clicked.connect(self.show_union_view)
                self.btn_calendar.clicked.connect(self.show_calendar_only)
                self.btn_task.clicked.connect(self.show_task_only)
        def show_calendar_only(self):
                self.task_side.setHidden(True)
                self.calendar_main.setHidden(False)
        
        def show_task_only(self):
                self.task_side.setHidden(False)
                self.calendar_main.setHidden(True)

        def show_union_view(self):
                self.task_side.setHidden(False)
                self.calendar_main.setHidden(False)



if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

