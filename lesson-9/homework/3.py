import json
import csv

def load_tasks(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

def save_tasks(file_name, tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task["priority"] for task in tasks) / total_tasks

    print("\nTask Statistics:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {average_priority:.2f}")

def convert_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "task", "completed", "priority"])
        writer.writeheader()
        writer.writerows(tasks)

json_file = "tasks.json"
csv_file = "tasks.csv"

tasks = load_tasks(json_file)
display_tasks(tasks)

calculate_stats(tasks)

convert_to_csv(json_file, csv_file)
print(f"Tasks converted to {csv_file}.")