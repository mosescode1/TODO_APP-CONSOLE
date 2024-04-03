import json


class FileStorage:
    __storage_dict = {}
    __file_path = "todo_storage"

    def all(self):
        return FileStorage.__storage_dict #Whole dictionary

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__storage_dict[key] = obj

    def save(self):
        objects = {}

        for key, value in FileStorage.__storage_dict.items():
            objects[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects, file, indent=4)

    def reload(self):
        from models.todo_model import Todo

        try:
            with open(FileStorage.__file_path, "r") as file:
                loaded_content = file.read()
            if loaded_content:
                # it has been deserialized here
                loaded_dict = json.loads(loaded_content)
                for value in loaded_dict.values():
                    self.new(Todo(**value))
        except FileNotFoundError:
            pass
