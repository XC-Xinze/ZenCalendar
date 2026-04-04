import json
import shutil
import datetime
from datetime import datetime
from backend import CalEvent, CalTask

file_path = "./data/"
class CalManager:
        def __init__(self, filename = "calendar_data.json"):
                self.filename = file_path + filename
                print(self.filename)
                self.event = CalEvent.CalEvent_list
                self.task = CalTask.CalTask_list

        def load(self):
                # forbiden load twice
                CalEvent.CalEvent_list.clear()
                CalTask.CalTask_list.clear()
                try:
                        with open(self.filename, 'r', encoding='utf-8') as f:
                                content = f.read()
                                # read return a string
                                if not content:
                                        return
                                dictdata = json.loads(content)
                                for item in dictdata.get("Events", []):
                                        CalEvent(
                                                title=item['title'],
                                                description=item['description'],
                                                custom_date=item['custom_date'],
                                                start_time=item['start_time'],
                                                end_time = item['end_time'],
                                                uid = item['uid']
                                        )
                                for item in dictdata.get('Tasks',[]):
                                        temp_task = CalTask(
                                                title=item['title'],
                                                description=item['description'],
                                                custom_date=item['custom_date'],
                                                uid = item['uid'],
                                        )
                                        temp_task.is_completed = item['is_completed']
                                print("Load Success")
                except FileNotFoundError:
                        print("No Such file. Create initial calendar.")
                except (json.JSONDecodeError, KeyError,ValueError) as e:
                        print(f"Saved calendar is ruined because of {e}. Backup for you and create new calendar.")
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        backup_name = f"backup_corrupted_{timestamp}.json"
                        shutil.move(self.filename, backup_name)
                        print(f"Backup file:{backup_name}")
                        self.event.clear()

        def save(self):
                all_data = {
                        "Events": [event.to_dict() for event in CalEvent.CalEvent_list],
                        "Tasks": [task.to_dict() for task in CalTask.CalTask_list]
                }

                with open(self.filename, 'w', encoding= 'utf-8') as f:
                        json.dump(all_data,f, ensure_ascii=False, indent=4)
                print("data saved.")

        def find_items_id(self,item_list, item_id):
                for item in item_list:
                        if str(item.id) == str(item_id):
                                return item
                return None


        def delete_id_item(self, item_list, item_id):
                for item in item_list:
                        if str(item.id) == str(item_id):
                                sure = input("Do you really want to remove this item? y/n")
                                while True:
                                        #move statement out of loop
                                        if sure == 'y' or sure == 'n':
                                                break
                                        else:
                                                sure = input("Please input y or n:")               
                                if sure == 'y':
                                        item_list.remove(item)
                                        self.save()
                                        return True
                                elif sure == 'n':
                                        return False
                print("No such item.")
                return False

        def show_item(self):
                print("\n" + "="*30)
                print("Calendar List")
                print("="*30)
                print("\n[Events]")
                for i,e  in enumerate(self.event):
                        print(f"-{i+1} {e.custom_date} | {e.title} | ({e.start_time} - {e.end_time})")

                print("\n[Task]")
                for i,t in enumerate(self.task):
                        status = "[x]" if t.is_completed else "[ ]"
                        print(f"-{i+1} {status} {t.title} End: {t.custom_date}")
                print("="*30 + "\n")
        def show_all_items(self):
                self.temp_all_items = CalEvent.CalEvent_list + CalTask.CalTask_list

                for i, item in enumerate(self.temp_all_items,1):
                        tag = "[E]" if isinstance(item,CalEvent) else "[T]"
                        print(f"{i} - {tag} {item.title}")

                        
        def search(self, keyword):
                print(f"\n ---- \"{keyword}\" results ----")
                results_event = [item for item in self.event if keyword.lower() in item.title.lower()]
                results_task = [item for item in self.task if keyword.lower() in item.title.lower()]

                if not results_event and not results_task:
                        print("There is no any relevant result.")
                if results_event:
                        print("==== Events ====")
                        for i, item in enumerate(results_event):
                                print(f"{i+1}: {item.title}")
                if results_task:
                        print("==== Tasks ====")
                        for i, item in enumerate(results_task):
                                print(f"{i+1}: {item.title}")
        @staticmethod
        def is_date_valid(date_str):
                try:
                        datetime.strptime(date_str, "%Y%m%d")
                        return True
                except ValueError:
                        return False
                
