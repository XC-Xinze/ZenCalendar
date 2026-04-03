import components
import manager
import datetime
from datetime import datetime, timedelta

def get_user_date(date_type = None):
        while True:
                user_input = input(f"{date_type}:YYYYMMDD or press Enter for today:").strip()

                if not user_input:
                        return datetime.now().strftime("%Y%m%d")
                if manager.is_date_valid(user_input):
                        return user_input
                else:
                        print("Wrong format of date.")

manager = manager.CalManager()
manager.load()

while True:
        print("\n1.Add task 2. Add event 3.Check task 4. Show all items 5.Search q.Quit\n")
        choice = input("Option: ")
        if choice == '1':
                title = input("Input title:")
                description = input("Input description:")
                custom_date = get_user_date("Target time")
                components.CalTask(title,description,custom_date, uid=None)
                manager.save()
        elif choice == '2':
                title = input("Input title:")
                description = input("Input description:")
                custom_date = get_user_date("Target time") 
                start_time = get_user_date("Start time") 
                end_time = get_user_date("End time")
                components.CalEvent(title,description,custom_date, start_time,end_time,uid = None)
                manager.save()
        elif choice == '3':
                manager.show_item()
                try:
                        idx = int(input("Choose the task you want:")) - 1
                        target = manager.task[idx]
                        target.checkbox()
                        manager.save()
                        print(f"Update No.{idx+1} task")
                except(IndexError, ValueError):
                        print("Invalid Augment!")
        elif choice == '4':
                manager.show_item()
        elif choice == '5':
                keyword = input("Input your keyword:")
                manager.search(keyword)
        elif choice == 'q':
                break
        