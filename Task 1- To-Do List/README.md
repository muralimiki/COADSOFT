#  Python To-Do List Application

A simple and efficient command-line based To-Do List application developed using Python and Object-Oriented Programming (OOP) concepts. This application helps users manage daily tasks by allowing them to add, view, update, delete, and mark tasks as completed.

---

#  Project Overview

The To-Do List Application is designed to improve task management and productivity. It provides a user-friendly command-line interface where users can organize their tasks efficiently.

The project demonstrates the implementation of:
- Python programming fundamentals
- Object-Oriented Programming (OOP)
- File handling using JSON
- Modular programming structure
- Data persistence

This project is ideal for beginners learning Python and software development concepts.

---

#  Features

- Add new tasks  
- View all tasks  
- Delete tasks  
- Mark tasks as completed  
- Persistent task storage using JSON  
- Modular and scalable code structure  
- Command-line interface (CLI)  
- Easy to customize and expand  

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| JSON | Data Storage |
| OOP Concepts | Code Structure & Reusability |
| VS Code | Development Environment |

---

#  Project Structure

```text
todo_app/
│
├── main.py
├── task.py
├── task_manager.py
├── storage.py
├── tasks.json
└── README.md
```

---
##  Run the Application

```bash
python main.py
```

#  Application Menu

```text
===== TO-DO LIST MENU =====

1. View Tasks
2. Add Task
3. Delete Task
4. Mark Task as Completed
5. Exit
```

---

#  Data Storage

Tasks are stored in a JSON file:

```text
tasks.json
```

Example:

```json
[
    {
        "title": "Complete project report",
        "completed": false
    }
]
```

This ensures that tasks remain saved even after closing the application.

---

#  Sample Output

```text
===== TO-DO LIST MENU =====

1. View Tasks
2. Add Task
3. Delete Task
4. Mark Task as Completed
5. Exit

Enter your choice: 2

Enter task title: Learn Python OOP

Task added successfully!
```

---

# Workflow of the Application

1. User selects an option from the menu
2. Application performs the requested operation
3. Task data is updated
4. Data is saved to JSON file
5. Updated tasks are displayed

---

# Future Enhancements

The project can be improved further by adding:

- GUI using Tkinter
- SQLite database integration
- User authentication system
- Task priorities
- Due dates & reminders
- Web or mobile version

---

#  Learning Outcomes

Through this project, the following concepts were learned:

- Python programming basics
- Object-Oriented Programming
- File handling
- JSON operations
- Modular coding practices
- CLI application development

---
