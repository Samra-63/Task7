import file_handler
def add_task(task):
    tasks = file_handler.read_tasks()
    tasks.append(task)
    file_handler.write_tasks(tasks)
    print("Task added successfully!")
def remove_task(index):
    tasks = file_handler.read_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        file_handler.write_tasks(tasks)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number. Please try again.")
def update_task(index, new_task):
    tasks = file_handler.read_tasks()
    if 0 <= index < len(tasks):
        old_task = tasks[index]
        tasks[index] = new_task
        file_handler.write_tasks(tasks)
        print(f"Updated task: '{old_task}' → '{new_task}'")
    else:
        print("Invalid task number. Please enter a valid one.")
def view_tasks():
    tasks = file_handler.read_tasks()
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found. Start adding some!")
