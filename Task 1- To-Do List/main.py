from task_manager import TaskManager

def menu():
    print("\n***TO-DO LIST MENU***")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def main():
    manager = TaskManager()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.view_tasks()

        elif choice == "2":
            title = input("Enter task title: ")
            manager.add_task(title)
            print("Task added successfully!")

        elif choice == "3":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                manager.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()