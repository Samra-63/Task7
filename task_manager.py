import task_operations
def main():
    while True:
        print("\nTask Manager")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Update a Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a new task: ")
            task_operations.add_task(task)
        elif choice == "2":
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                task_operations.remove_task(index)
            except ValueError:
                print("Oops! Please enter a valid number.")
        elif choice == "3":
            try:
                index = int(input("Enter the task number to update: ")) - 1
                new_task = input("Enter the updated task: ")
                task_operations.update_task(index, new_task)
            except ValueError:
                print("Oops! Please enter a valid number.")
        elif choice == "4":
            task_operations.view_tasks()
        elif choice == "5":
            print("Goodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
