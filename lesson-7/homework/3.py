import csv
import json
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return (f"{self.task_id}, {self.title}, {self.description}, "
                f"{self.due_date or 'No Due Date'}, {self.status}")

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("due_date"),
            data.get("status", "Pending")
        )


class FileHandler:
    """Abstract class for file handling."""
    def save_tasks(self, file_name, tasks):
        raise NotImplementedError

    def load_tasks(self, file_name):
        raise NotImplementedError


class CSVHandler(FileHandler):
    """CSV implementation of FileHandler."""
    def save_tasks(self, file_name, tasks):
        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            
            for task in tasks:
                writer.writerow(task.to_dict())

    def load_tasks(self, file_name):
        tasks = []
        try:
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks


class JSONHandler(FileHandler):
    """JSON implementation of FileHandler."""
    def save_tasks(self, file_name, tasks):
        with open(file_name, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load_tasks(self, file_name):
        tasks = []
        try:
            with open(file_name, "r") as file:
                data = json.load(file)

                for item in data:
                    tasks.append(Task.from_dict(item))

        except FileNotFoundError:
            pass

        return tasks


class ToDoApp:
    def __init__(self, file_handler, file_name):
        self.file_handler = file_handler
        self.file_name = file_name
        self.tasks = self.file_handler.load_tasks(self.file_name)

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("Tasks:")

        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")

        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input(f"Enter new Title (current: {task.title}): ") or task.title
                task.description = input(f"Enter new Description (current: {task.description}): ") or task.description
                task.due_date = input(f"Enter new Due Date (current: {task.due_date}): ") or task.due_date
                task.status = input(f"Enter new Status (current: {task.status}): ") or task.status
                print("Task updated successfully!")
                return
            
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")

        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
            
        print("Task not found.")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        
        if not filtered_tasks:
            print(f"No tasks found with status: {status}")
            return
        
        print(f"Tasks with status {status}:")
        
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.file_handler.save_tasks(self.file_name, self.tasks)
        print("Tasks saved successfully!")

    def menu(self):
        while True:
            print("\nTo-Do Application")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Exit")

            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Goodbye!")
                self.save_tasks()
                break
            else:
                print("Invalid choice. Please try again.")

print("Choose file format for storage:")
print("1. CSV")
print("2. JSON")

choice = input("Enter your choice: ")

if choice == "1":
    handler = CSVHandler()
    file_name = "tasks.csv"
elif choice == "2":
    handler = JSONHandler()
    file_name = "tasks.json"
else:
    print("Invalid choice. Defaulting to JSON format.")
    handler = JSONHandler()
    file_name = "tasks.json"

app = ToDoApp(handler, file_name)
app.menu()