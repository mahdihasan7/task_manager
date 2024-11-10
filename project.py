tasks = []  # Global list to store tasks
next_task_id = 1  # Variable to keep track of unique task IDs

def main():
    print("Welcome to Task Manager!")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (high, medium, low): ")
            add_task(task_name, due_date, priority)
            print("Task added successfully!")

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            task_id = input("Enter the task ID to mark as complete: ")
            complete_task(task_id)
            print("Task marked as complete!")

        elif choice == '4':
            export_tasks_to_txt()
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def add_task(task_name, due_date, priority):
    global next_task_id

    task = {
        "id": next_task_id,
        "name": task_name,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    next_task_id += 1

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    priority_order = {'high': 1, 'medium': 2, 'low': 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order[x['priority']])

    print("\nTask List:")
    for task in sorted_tasks:
        completion_status = "Completed" if task["completed"] else "Incomplete"
        print(f"ID: {task['id']}, Name: {task['name']}, Due Date: {task['due_date']}, "
              f"Priority: {task['priority'].capitalize()}, Status: {completion_status}")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == int(task_id):
            task['completed'] = True
            return
    print(f"Task with ID {task_id} not found.")

def export_tasks_to_txt():
    """Exports all tasks to a text file before exiting the program."""
    with open("tasks.txt", "w") as file:
        file.write("Task List:\n")
        for task in tasks:
            completion_status = "Completed" if task["completed"] else "Incomplete"
            task_info = (
                f"ID: {task['id']}, Name: {task['name']}, Due Date: {task['due_date']}, "
                f"Priority: {task['priority'].capitalize()}, Status: {completion_status}\n"
            )
            file.write(task_info)
    print("All tasks have been saved to tasks.txt")

if __name__ == "__main__":
    main()
