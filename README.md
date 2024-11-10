# Study Helper

## [Video Demo](https://youtu.be/YZLX66BVPFg)

### Description:
This project is a simple task manager, which allows users to add tasks, mark added tasks as completed, view all the tasks. After the user choose to exit the program, the program will create a new txt file on all of the logs. The project was created as part of CS50's introduction to programming with python, that teaches beginners how to write code in the wonderful language of python.

### How the Program Works:
The Task Manager program allows users to create, view, and manage tasks. Each task has a name, due date, priority level, and a completion status. The program uses a simple menu interface where users can add tasks, view all tasks sorted by priority, and mark tasks as complete. Before the user exits, the program saves all tasks to a tasks.txt file, which is overwritten each time the program restarts, so it only includes tasks from the current session.

### Project Files:
- `project.py`: Contains the python code of the project.
- `test_project.py`: A pytest implemention code of the project.

### Design Choices:
There really isn't much of a design in the file. It operates on the terminal window

### Features:
- Create tasks.
- View tasks.
- Mark tasks as completed.
- Output's the logs in a tasks.txt file.

### Challenges:
The most challenging part of the project was keeping track of the tasks and assigning each task an unique id.

### Installation:
After downloading the project repository, navigate to the folder using the terminal:

```
$ cd task_manager
```
Open VScode in the directory:

```
$ code .
```

You need to have python extension installed. Open new terminal from the options at the top. Run the program using python project.py or python3 project.py or py project.py

### Usage:
Once the program is running, you will see a bunch of options 1, 2, 3, 4 with options what you wish to do.

>[!IMPORTANT]
> The program must be run at terminal window.
