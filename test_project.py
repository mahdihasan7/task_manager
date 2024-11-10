from project import add_task, view_tasks, complete_task, tasks

# Test add_task function
def test_add_task():
    initial_task_count = len(tasks)
    add_task("Test Task", "2024-12-01", "high")
    assert len(tasks) == initial_task_count + 1
    assert tasks[-1]["name"] == "Test Task"
    assert tasks[-1]["due_date"] == "2024-12-01"
    assert tasks[-1]["priority"] == "high"
    assert tasks[-1]["completed"] == False

# Test view_tasks function (capturing printed output)
def test_view_tasks(capsys):
    add_task("Task 1", "2024-12-01", "high")
    add_task("Task 2", "2024-11-15", "low")

    # Call view_tasks() which will print the tasks
    view_tasks()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if tasks are displayed correctly in the output
    assert "Task List:" in captured.out
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out

# Test complete_task function
def test_complete_task():
    add_task("Complete Me", "2024-11-10", "medium")
    task_id = tasks[-1]["id"]

    # Mark the task as complete
    complete_task(task_id)
    assert tasks[-1]["completed"] == True  # The task should be marked as completed

    # Try to mark a non-existent task as complete
    complete_task(999)  # Non-existent task ID
    # Ensure the task's completed status remains True
    assert tasks[-1]["completed"] == True
