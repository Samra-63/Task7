import os
def ensure_file_exists(filename="tasks.txt"):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            pass
def read_tasks(filename="tasks.txt"):
    ensure_file_exists(filename)
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
def write_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
