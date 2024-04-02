from models.todo_model import Todo
new = Todo()
new.create_todo("name", "Texted")
new.to_dict()
new.save()
