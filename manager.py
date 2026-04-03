import json
import components
from components import CalEvent, CalTask


class CalManager:
        def __init__(self, filename = "calendar_data.json"):
                self.filename = filename
                self.event = CalEvent.CalEvent_list
                self.task = CalTask.CalTask_list

        def load(self):
                # forbiden load twice
                CalEvent.CalEvent_list.clear()
                CalTask.CalTask_list.clear()
                try:
                        with open(self.filename, 'r', encoding='utf-8') as f:
                                dict = json.load(f)
                                for item in dict.get("Events", []):
                                        CalEvent(
                                                title=item['title'],
                                                description=item['description'],
                                                custom_date=item['custom_date'],
                                                start_time=item['start_time'],
                                                end_time = item['item_date'],
                                                uid = item['uid']
                                        )
                                for item in dict.get('Tasks',[]):
                                        temp_task = CalTask(
                                                title=item['title'],
                                                description=item['description'],
                                                custom_date=item['custom_date'],
                                                uid = item['uid'],
                                        )
                                        temp_task.is_completed = item['is_completed']
                                print("Load Success")
                except FileNotFoundError:
                        print("No Such file")

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
                                self.task.remove(item)
                                self.save()
                                return True
                return False
                
        def show_item(self):
                print("\n" + "="*30)
                print("Calendar List")
                print("="*30)
                
                print("\n[Events]")
                for e in self.event:
                        print(f"- {e.custom_date} | {e.title} | ({e.start_time} - {e.end_time})")
                
                print("\n[Task]")
                for t in self.task:
                        status = "[x]" if t.is_completed else "[ ]"
                        print(f"{status} {t.title} End: {t.custom_date}")
                print("="*30 + "\n")