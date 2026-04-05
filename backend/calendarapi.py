from backend import CalManager, CalEvent, CalTask
from datetime import datetime

class CalendarAPI:
    def __init__(self,manager:CalManager):
        self.manager = manager

    def get_all_tasks(self):
        return [task.to_dict() for task in self.manager.task]

    def get_all_events(self):
        return [event.to_dict() for event in self.manager.event]
# task operation
    def create_task(self, title, description ="", custom_date = None):
        title = title.strip()

        if not title:
            return {
                "success": False,
                "error": "Title cannot be empty."
            }
        
        if custom_date == None:
            custom_date = datetime.now().strftime("%Y%m%d")

        new_task = CalTask(
            title=title,
            description=description,
            custom_date=custom_date,
            uid=None,
            linked_event_id = None
        )

        self.manager.save()
        return {
            "success": True,
            "data": new_task.to_dict()
        }

    def delete_task(self):
        return None

    def check_task(self, task_id):
        target_task = self.manager.find_items_id(self.manager.task, task_id)
        if target_task is None:
            return{
                "success": False,
                "error": "Task not found."
            }
        
        target_task.checkbox()
        self.manager.save()

        return {
            "success": True,
            "data": target_task.to_dict()
        }


# event operation

    def create_event():
        return None

    def delete_event():
        return None


    