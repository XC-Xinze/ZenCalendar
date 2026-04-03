import manager
import sys
import components
import datetime
from datetime import datetime

class ZenMenu:
        def __init__(self,manager):
                self.manager = manager
                self.manager.load()
                self.menu = {
                        "1": self.add_event,
                        "2": self.add_task,
                        "3": self.delete_item,
                        "4": self.show_item,
                        "5": self.check_task_status,
                        "6": self.seach_item,
                        "q": self.exit_app
                }

        def print_menu(self):
                print(f"\n{'='*20} 📅 ZenCalendar {'='*20}")
                print("1. Add event")
                print("2. Add task")
                print("3. Delete item")
                print("4. Show all item")
                print("5. Mark task")
                print("6. Search item")
                print("q. EXIT")
                print("="*50)
        def run_zen(self):
                while True:
                        self.print_menu()
                        choice = input("Option:")
                        action = self.menu.get(choice)
                        if action:
                                action()

        def get_user_date(self,date_type = None):
                while True:
                        user_input = input(f"{date_type}:YYYYMMDD or press Enter for today:").strip()

                        if not user_input:
                                return datetime.now().strftime("%Y%m%d")
                        if self.manager.is_date_valid(user_input):
                                return user_input
                        else:
                                print("Wrong format of date.")
        def add_task(self):
                title = input("Input title:")
                description = input("Input description:")
                custom_date = self.get_user_date("Target time")
                components.CalTask(title,description,custom_date, uid=None)
                self.manager.save()
        
        def add_event(self):
                title = input("Input title:")
                description = input("Input description:")
                custom_date = self.get_user_date("Target time") 
                start_time = self.get_user_date("Start time") 
                end_time = self.get_user_date("End time")
                components.CalEvent(title,description,custom_date, start_time,end_time,uid = None)
                self.manager.save()

        def delete_item(self):
                self.manager.show_all_items()
                try:
                        idx = int(input("Choose the item you want to remove:")) - 1
                        target = self.manager.temp_all_items[idx]
                        if isinstance(target, components.CalEvent):
                                        self.manager.delete_id_item(components.CalEvent.CalEvent_list, target.id)
                        else:
                                        self.manager.delete_id_item(components.CalTask.CalTask_list, target.id)
                except IndexError:
                        print("Wrong Index.")
                except ValueError:
                        print("Only numberic input.")
        def show_item(self):
                self.manager.show_item()


        def check_task_status(self):
                self.manager.show_item()
                try:
                        idx = int(input("Choose the task you want:")) - 1
                        target = self.manager.task[idx]
                        target.checkbox()
                        self.manager.save()
                        print(f"Update No.{idx+1} task")
                except(IndexError, ValueError):
                        print("Invalid Augment!")
        def seach_item(self):
                keyword = input("Input your keyword:")
                self.manager.search(keyword)
        
        def exit_app(self):
                self.manager.save()
                sys.exit()