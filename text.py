from models.todo_model import Todo
new = Todo()
# new.create_todo("name", "Texted")
new.to_dict()
new.create_task("EATING", "BY 9 AM")
new.save()
