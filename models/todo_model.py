from datetime import datetime
from uuid import uuid4


class Todo:
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at" or key == "completed_at":
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.task = {}

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the current datetime """
        from models import storage

        storage.new(self)
        storage.save()

    def create_task(self, task_title, task_description):
        """ """
        self.task[task_title] = task_description  # No need to put self, to parameters, as they are outside vars
        self.task["completed"] = False

    def completed(self):
        self.__dict__["completed_at"] = datetime.utcnow()
        self.task["completed"] = True

    def to_dict(self):
        object = self.__dict__.copy()
        object["created_at"] = object["created_at"].isoformat()
        if "completed_at" in object:
            object["completed_at"] = object["completed_at"].isoformat()
        # object[Todo.task_number] = self.create_todo()
        return object

#    @staticmethod
#    def strike(text):
#        text =  ''.join([u'\u0336{}'.format(c) for c in text])
#        print(text)
