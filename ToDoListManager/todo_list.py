# todo_list.py

class Task:
    def __init__(self, name, status="Pending"):
        self.name = name.lower()
        self.status = status

    def __str__(self):
        return f"{self.name.capitalize()} - {self.status}"

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                task.status = "Completed"

    def clear_tasks(self):
        self.tasks.clear()
        
    def delete_task(self,task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]


    def get_tasks(self):
        return self.tasks
