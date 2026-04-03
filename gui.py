from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt

class CalendarBaseDisplay(QFrame):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setObjectName("ZenCalendar")
                self.set_base_style
        
        def set_base_style(self):
                self.setStyleSheet("""
                        #ZenCalendar{
                                background-color: white;
                                border-radius: 15px;
                                border: 1px solid #E0E0E0;
                                }
                        #ZenCalendar:hover {
                                border: 1px solid #1A73E8;
                                   }
                                   """)

class CalendarPage(CalendarBaseDisplay):
        def __init__(self, parent=None):
                super().__init__(parent)
                layout = QVBoxLayout(self)
                layout.addWidget(QLabel("This is calendar view"))


class CalendarTaskPage(CalendarBaseDisplay):
        def __init__(self, parent=None):
                super().__init__(parent)
                layout = QVBoxLayout(self)
                layout.addWidget(QLabel("This is task view"))