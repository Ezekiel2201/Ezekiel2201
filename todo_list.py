todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "Status": "Pending"})
    print(f'Task "{task}" added to the list.\n')


def view_tasks():
    print("Your todo list:")
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}: {task['task']} - {task['Status']}")
    print('\n')


def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove.")
    else:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f'Task "{removed_task["task"]}" removed from the list.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def mark_completed():
    if len(todo_list) == 0:
        print("No tasks to mark as completed.")
    else:
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]["Status"] = "Completed"
                print(f'Task "{todo_list[task_number - 1]["task"]}" marked as completed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def menu():
    while True:
        print("\nTodo List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        choice = input("\n Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print_welcome_message()
    menu()


