from PyQt6.QtWidgets import QListWidget, QLineEdit,QPushButton, QWidget, QGridLayout,QHBoxLayout, QVBoxLayout, QLabel, QFrame
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
import calendar
from datetime import datetime
from components import CalTask
import manager
class CalendarBaseDisplay(QFrame):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.setObjectName("ZenCalendar")
                self.set_base_style()
        
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
        def __init__(self, manager_gui,parent=None):
                super().__init__(parent)
                self.manager_gui = manager_gui

                self.layout = QVBoxLayout(self)
                self.layout.setContentsMargins(10,10,10,10)
                self.layout.setSpacing(10)
                 # get date
                now = datetime.now()
                self.display_year = now.year
                self.display_month = now.month

                self.grid_widget = QWidget()
                self.grid_layout = QGridLayout(self.grid_widget)
                self.grid_layout.setSpacing(0)
                # year month
                self.setup_nav_header()
                # weekday
                self.setup_weekday_header()


                # add grid
                
                self.layout.addWidget(self.grid_widget)
                self.prev_btn.clicked.connect(self.prev_month)
                self.next_btn.clicked.connect(self.next_month)
                self.refresh_calendar()
        def setup_nav_header(self):
                nav_layout = QHBoxLayout()
                self.prev_btn = QPushButton("<")
                self.next_btn = QPushButton(">")
                text = f"Year. {self.display_year}  Month. {self.display_month}"
                self.month_label = QLabel(text)
                self.month_label.setStyleSheet("font-size: 18px; font-weight: bold;")

                nav_layout.addWidget(self.prev_btn)
                nav_layout.addStretch()
                nav_layout.addWidget(self.month_label)
                nav_layout.addStretch()
                nav_layout.addWidget(self.next_btn)

                self.layout.addLayout(nav_layout)

        def setup_weekday_header(self):
                weeks_layout = QHBoxLayout()
                week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

                for day in week_days:
                        label = QLabel(day)
                        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        label.setStyleSheet("color: #70757a; font-weight: bold; padding: 5px;")
                        weeks_layout.addWidget(label)
                self.layout.addLayout(weeks_layout)

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
        def prev_month(self):
                if self.display_month == 1:
                        self.display_month = 12
                        self.display_year -= 1
                else:
                        self.display_month -= 1
                self.update_display()

        def next_month(self):
                if self.display_month ==12:
                        self.display_month = 1
                        self.display_year += 1
                else:
                        self.display_month += 1
                self.update_display()

        def update_display(self):
                self.month_label.setText(f"Year. {self.display_year} Month. {self.display_month}")
                self.refresh_calendar()
class CalendarTaskPage(CalendarBaseDisplay):
        def __init__(self, manager_gui, parent=None):
                super().__init__(parent)
                self.manager_gui = manager_gui

                self.input_field = QLineEdit()
                self.input_field.setPlaceholderText("Input task's contents...")
                self.btn_enter = QPushButton("Enter")
                self.btn_delete_task = QPushButton("Delete")
                self.tasks_list_widget = QListWidget()
                
                layout = QVBoxLayout(self)
                layout.addWidget(QLabel("Tasks list"))
                layout.addWidget(self.input_field)
                layout.addWidget(self.btn_enter)
                layout.addWidget(self.tasks_list_widget)
                layout.addWidget(self.btn_delete_task)

                self.tasks_list_widget.itemDoubleClicked.connect(self.toggle_task_status)
                self.input_field.returnPressed.connect(self.add_task_to_list)
                self.btn_enter.clicked.connect(self.add_task_to_list)
                self.btn_delete_task.clicked.connect(self.delete_task)

 #               self.load_tasks_from_json()

                self.setStyleSheet("background-color: #e0b0f0;border: 1px solid green;")
                self.load_tasks_to_list()
        def delete_task(self):
                row = self.tasks_list_widget.currentRow()
                if row <0:
                        return
                target_task = self.manager_gui.task[row]
                reply = QMessageBox.question(
                        self,
                        "Confirm Delete",
                        f"Do you really want to delete this task?\n\n{target_task.title}",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                        QMessageBox.StandardButton.No
                        )
                if reply == QMessageBox.StandardButton.Yes:
                        self.manager_gui.task.remove(target_task)
                        self.manager_gui.save()
                        self.load_tasks_to_list()
        def toggle_task_status(self, item):
                row = self.tasks_list_widget.row(item)
                target_task = self.manager_gui.task[row]

                target_task.checkbox()
                self.manager_gui.save()
                self.load_tasks_to_list()

        def load_tasks_to_list(self):
                self.tasks_list_widget.clear()

                for task in self.manager_gui.task:
                        status = "[x]" if task.is_completed else "[ ]"
                        text = f"{status} - {task.title} | Due: {task.custom_date}"
                        self.tasks_list_widget.addItem(text)
        def add_task_to_list(self):
                title = self.input_field.text().strip()
                if not title:
                        return
                today_str = datetime.now().strftime("%Y%m%d")
                CalTask(
                        title=title,
                        description="",
                        custom_date=today_str,
                        uid=None
                )

                self.manager_gui.save()
                self.load_tasks_to_list()
                self.input_field.clear()
