import datetime
from datetime import datetime
import uuid

class CalComponents:
        def __init__(self, title, description, custom_date = None, uid = None):
                self.title = title
                self.description = description
                self.create_date = datetime.today()
                self.custom_date = custom_date
                # load file will re-write uid so change it to the parameter
                self.id = uid if uid else uuid.uuid4()
        
        def update_basic(self, new_title = None, new_description = None):
                if new_title and new_title!= self.title:
                        self.title = new_title
                if new_description and new_description != self.description:
                        self.description = new_description
                print("basic info has updated!")

        def update_custom_date(self, custom_date):
               if custom_date:
                       self.custom_date = custom_date
        def to_dict(self):
                return {
                        "title": self.title,
                        "description": self.description,
                        "create_date": self.create_date.isoformat(),
                        "custom_date": self.custom_date,
                        "uid": str(self.id)
                }

class CalEvent(CalComponents):
        CalEvent_list = []
        def __init__(self, title, description, custom_date,  start_time = None, end_time = None, uid = None):
                super().__init__(title, description, custom_date,uid)
                self.start_time = start_time
                self.end_time = end_time
                CalEvent.CalEvent_list.append(self)

        def to_dict(self):
                temp_dict = super().to_dict()
                temp_dict["start_time"] = self.start_time
                temp_dict["end_time"] = self.end_time
                return temp_dict




class CalTask(CalComponents):
        CalTask_list = []
        def __init__(self, title, description, custom_date,uid):
                super().__init__(title, description, custom_date,uid)
                self.is_completed = False
                CalTask.CalTask_list.append(self)
                
        def checkbox(self):
               self.is_completed = not self.is_completed

        def to_dict(self):
                temp_dict = super().to_dict()
                temp_dict["is_completed"] = self.is_completed
                return temp_dict