from datetime import datetime
from uuid import uuid4


class Todo:

    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the current datetime """
        from models import storage
        self.updated_at = datetime.utcnow()

        storage.new(self)
        storage.save()

    def create_todo(self, todo_name, text):
        self.todo_name = todo_name
        self.text = text

    def to_dict(self):
        object = self.__dict__.copy()
        object["created_at"] = object["created_at"].isoformat()
        object["updated_at"] = object["updated_at"].isoformat()
        return object
