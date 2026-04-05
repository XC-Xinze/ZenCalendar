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

    def delete_task(self, task_id):
        success = self.manager.web_delete_id_item(self.manager.task,task_id)
        if not success:
            return {
                "success": False,
                "error": "This task is no longer exist"
            }
        return {
            "success": True,
            "message": "Task has been removed." 
        }

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

    def create_event(self, title, description = "",start_time=None, end_time = None, custom_date = None, uid = None,linked_task_id = None):
        title = title.strip()
        if not title:
            return {
                "success": False,
                "error": "Title cannot be empty"
            }
        if custom_date is None:
            custom_date = datetime.now().strftime("%Y%m%d")
        new_event = CalEvent(
            title=title,
            description=description,
            uid=uid,
            start_time=start_time,
            end_time=end_time,
            custom_date=custom_date,
            linked_task_id=linked_task_id
        )
        self.manager.save()
        return {
            "success": True,
            "data": new_event.to_dict()
        }

    def delete_event(self, event_id):
        success = self.manager.web_delete_id_item(self.manager.event,event_id)
        if not success:
            return {
                "success": False,
                "error": "This event is not exist"
            }
        return {
            "success": True,
            "message": "Event has been removed"
        }


    