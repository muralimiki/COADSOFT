from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted task: {removed.title}")
        else:
            print("Invalid task number.")
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    def save_tasks(self):
        Storage.save(self.tasks)
    def load_tasks(self):
        data = Storage.load()
        self.tasks = [Task.from_dict(item) for item in data]