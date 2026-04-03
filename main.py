import components
import manager

manager = manager.CalManager()
manager.load()

while True:
        print("\n1.Add task 2. Add event 3.Check task 4. Show all items 5.Quit\n")
        choice = input("Option: ")
        if choice == '1':
                title = input("Input title:")
                description = input("Input description:")
                custom_date = input("Input date:")
                components.CalTask(title,description,custom_date, uid=None)
                manager.save()
        elif choice == '2':
                title = input("Input title:")
                description = input("Input description:")
                custom_date = input("Input date:")
                start_time = input("Start time:")
                end_time = input("End time:")
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
                break
        