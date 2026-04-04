from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
import calendar
from datetime import datetime

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

                # add grid
                self.grid_layout = QGridLayout(self)
                self.grid_layout.setSpacing(0)
                self.grid_layout.setContentsMargins(0,0,0,0)
                
                # get date
                now = datetime.now()
                self.display_year = now.year
                self.display_month = now.month
                self.refresh_calendar()

        def refresh_calendar(self):
                while self.grid_layout.count():
                        item = self.grid_layout.takeAt(0)
                        if item.widget():
                                item.widget().deleteLater()
                first_day_weekday, num_days = calendar.monthrange(self.display_year,self.display_month)
                for i in range(42):
                        row = i // 7
                        col = i % 7

                        day_num = i - first_day_weekday + 1

                        cell = QFrame()
                        cell.setObjectName("CalendarCell")

                        style_str = "#CalendarCell { border: 0.5px solid #E0E0E0; background-color: white;}"

                        if 1 <= day_num <= num_days:
                                label_text = str(day_num)
                                if day_num == datetime.now().day and self.display_month == datetime.now().month:
                                        style_str += "#CalendarCell {background-color: #E8F0FE;}"
                        else:
                                label_text = ""
                                style_str += "#CalendarCell {background-color: #FDFDFD;}"
                        cell.setStyleSheet(style_str)

                        cell_layout = QVBoxLayout(cell)
                        date_label = QLabel(label_text)
                        date_label.setStyleSheet("font-weight: bold; color: #3C4043;")
                        cell_layout.addWidget(date_label,alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
                        cell_layout.addStretch()
                        self.grid_layout.addWidget(cell,row, col)

class CalendarTaskPage(CalendarBaseDisplay):
        def __init__(self, parent=None):
                super().__init__(parent)
                layout = QVBoxLayout(self)
                layout.addWidget(QLabel("This is task view"))
                self.setStyleSheet("background-color: #e0b0f0;border: 1px solid green;")