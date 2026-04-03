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

        def find_events_id(self, event_id):
                for event in self.event:
                        if str(event.id) == str(event_id):
                                return event
                return None

        def find_events_id(self, event_id):
                for event in self.event:
                        if str(event.id) == str(event_id):
                                return event 
                return None
        
        def find_tasks_id(self, task_id):
                for task in self.task:
                        if str(task.id) == str(task_id):
                                return task
                return None

        def delete_task_item(self, task_id):
                for task in self.task:
                        if str(task.id) == str(task_id):
                                self.task.remove(task)
                                self.save()
                                return True
                return False
                

                