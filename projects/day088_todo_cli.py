# Day 88 Project: To-Do List Manager
import json

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, title: str):
        item = {"id": len(self.todos) + 1, "title": title, "completed": False}
        self.todos.append(item)
        return item

    def complete(self, todo_id: int):
        for item in self.todos:
            if item["id"] == todo_id:
                item["completed"] = True
                return True
        return False

    def list_all(self):
        return self.todos

todo = TodoManager()
todo.add("Complete Day 88 coding")
todo.add("Commit changes to GitHub")
todo.complete(1)
print("Todos:", json.dumps(todo.list_all(), indent=2))
