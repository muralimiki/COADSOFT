# CODSOFT
# 📝 Python To-Do List Application

A simple and efficient command-line based To-Do List application developed using Python and Object-Oriented Programming (OOP) concepts. This application helps users manage daily tasks by allowing them to add, view, update, delete, and mark tasks as completed.

---

# 📖 Project Overview

The To-Do List Application is designed to improve task management and productivity. It provides a user-friendly command-line interface where users can organize their tasks efficiently.

The project demonstrates the implementation of:
- Python programming fundamentals
- Object-Oriented Programming (OOP)
- File handling using JSON
- Modular programming structure
- Data persistence

This project is ideal for beginners learning Python and software development concepts.

---

# 🚀 Features

✅ Add new tasks  
✅ View all tasks  
✅ Delete tasks  
✅ Mark tasks as completed  
✅ Persistent task storage using JSON  
✅ Modular and scalable code structure  
✅ Command-line interface (CLI)  
✅ Easy to customize and expand  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| JSON | Data Storage |
| OOP Concepts | Code Structure & Reusability |
| VS Code | Development Environment |

---

# 📂 Project Structure

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

# 🧠 OOP Concepts Used

## 1. Class
Classes are used to define the structure and behavior of tasks and task management.

### Classes Used:
- `Task`
- `TaskManager`
- `Storage`

---

## 2. Object
Objects are created from classes to manage individual tasks.

Example:
```python
task = Task("Complete Python project")
```

---

## 3. Encapsulation
Task operations are encapsulated inside methods such as:
- `add_task()`
- `delete_task()`
- `complete_task()`

---

## 4. Abstraction
The storage functionality is separated into a different file (`storage.py`) to hide implementation details.

---

# ⚙️ Installation & Setup

## Step 1: Install Python

Download and install Python:

https://www.python.org/downloads/

While installing:
- Enable **Add Python to PATH**

---

## Step 2: Clone Repository

```bash
git clone https://github.com/your-username/todo-app.git
```

---

## Step 3: Navigate to Project Folder

```bash
cd todo-app
```

---

## Step 4: Run the Application

```bash
python main.py
```

If `python` does not work:

```bash
python3 main.py
```

---

# ▶️ Application Menu

```text
===== TO-DO LIST MENU =====

1. View Tasks
2. Add Task
3. Delete Task
4. Mark Task as Completed
5. Exit
```

---

# 💾 Data Storage

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

# 📸 Sample Output

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

# 🔄 Workflow of the Application

1. User selects an option from the menu
2. Application performs the requested operation
3. Task data is updated
4. Data is saved to JSON file
5. Updated tasks are displayed

---

# 🚀 Future Enhancements

The project can be improved further by adding:

- GUI using Tkinter
- SQLite database integration
- User authentication system
- Task priorities
- Due dates & reminders
- Search and filter options
- Dark mode UI
- Web or mobile version

---

# 🎯 Learning Outcomes

Through this project, the following concepts were learned:

- Python programming basics
- Object-Oriented Programming
- File handling
- JSON operations
- Modular coding practices
- CLI application development

---

# 🐞 Common Errors & Solutions

## Error:
```text
No such file or directory
```

### Solution:
Make sure you are inside the correct project folder before running:

```bash
cd todo_app
python main.py
```

---

# 🤝 Contribution

Contributions are welcome!

If you'd like to improve this project:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

# 📄 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Murali G

Python Developer | Software Enthusiast

---

# ⭐ GitHub

If you found this project useful, please give it a ⭐ on GitHub!
