#!/usr/bin/python3
from cmd import Cmd
import sys
import shlex
from models.todo_model import Todo
from models import storage  # storage is instance of Filestorage


class Todocommand(Cmd):
    """
    ***This is our TODO CONSOLE***
    """

    def do_create(self, line):
        if not line:
            print("USAGE: <create> <class_name> <TASK>")
            return
        var = shlex.split(line)

        if len(var) < 2:
            print("USAGE: <create> <class_name> <TASK>")
            return
        todo = Todo()
        todo.create_task(var[0], var[1])
        todo.save()

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        pass  # Dont do anything

    def do_show(self, line):
        if not line:
            print("USAGE: <show> <class_name> <ID>")
            return
        var = line.split()
        if len(var) < 2:
            print("USAGE: <show> <class_name> <ID>")
            return
        key_id = f"{var[0]}.{var[1]}"  # string_format f"{}"
        for key, value in storage.all().items():
            if key == key_id:
                print(value.to_dict())

    def do_all(self, line):
        """ """
        for key, value in storage.all().items():
            print(key, value.to_dict())
    def do_mark(self, line):
        if not line:
            print("USAGE: <class_name> <I_D> <to_do_name> Missing")
            return
        var = line.split()
        if len(var) < 2:
            print("USAGE: <I_D> <to_do_name> Missing")
            return
        # if len(var) < 3:
        #     print("USAGE: <to_do_name> Missing")
        #     return
        key_id = f"{var[0]}.{var[1]}"  # string_format f"{}"
        for key, value in storage.all().items():
            if key == key_id:
                var = value.to_dict()
                # print(var)
                for keys, items in var["task"].items():
                    if isinstance(key, str) and isinstance(items, str):
                        print(keys, items)
                        var["task"] = ''.join([u'\u0336{}'.format(c) for c in keys])
                        items = ''.join([u'\u0336{}'.format(c) for c in items])
                        if key == "completed":
                            Todo.completed()
                            storage.save()
                        print(f"The todo {keys} {items} has been completed")
                    
                    # value["task"] = dict([items = strike(items) for items, values in value["task"])
                    # print(value.to_dict())

    def do_delete(self, line):
        if not line:
            print("USAGE: <class_name> <I_D> <to_do_name> Missing")
            return
        var = line.split()
        if len(var) < 2:
            print("USAGE: <I_D> <to_do_name> Missing")
            return
        # if len(var) < 3:
        #     print("USAGE: <to_do_name> Missing")
        #     return
        key_id = f"{var[0]}.{var[1]}"  # string_format f"{}"
        storage.all().pop(key_id)
        storage.save()
        
    def do_undone(self, line):
        pass
    
    def do_q(self, line):
        sys.exit(0)


if __name__ == "__main__":
    Todocommand().cmdloop()
