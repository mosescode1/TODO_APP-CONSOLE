#!/usr/bin/python3
from models.todo_model import Todo
new = Todo()
# new.create_todo("name", "Texted")
new.to_dict()
new.create_task("EATING", "BY 9 AM")
# new.strike("abcde")
new_1 = Todo()
new_1.to_dict()
new_1.create_task("READING", "BY 10 PM")
new.save()
new_1.save()
