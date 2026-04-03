import json
import components
from components import CalEvent, CalTask


class CalManager:
        def __init__(self, filename = "calendar_data.json"):
                self.filename = filename
                self.event = CalEvent.CalEvent_list
                self.task = CalTask.CalTask_list
        
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
                

                