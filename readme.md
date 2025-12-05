# README.md

# To-Do App (CLI Version)

A simple command-line based To-Do application built in Python. It supports user registration, login, task creation, task viewing, and marking tasks as completed.

This project is great for learning:

- Python file handling
- JSON storage
- CLI menus
- Basic authentication flow
- Clean program flow design

---

## Features

- User signup and login
- Tasks stored separately for each user
- Add new tasks with timestamp
- Auto-incrementing task IDs
- View all tasks
- Mark tasks as completed
- Clean terminal-based UI

---

## File Structure

```
project/
├── user.json          # stores usernames and passwords
├── user_tasks.json    # stores tasks per user
├── todo.py            # main program file
├── README.md
└── .gitignore
```

---

## Installation & Running

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/todo-cli-app.git
cd todo-cli-app
```

### 2. Run the program

```
python3 todo.py
```

---

## JSON Storage Format

### Users

```
[
  {
    "name": "Tamim",
    "password": "1234"
  }
]
```

### Tasks

```
{
  "Tamim": [
    {
      "id": 1,
      "time": "2025-01-01 12:00:00",
      "task_name": "Learn Python",
      "status": "pending"
    }
  ]
}
```

---

## Future Improvements

- Delete task
- Edit task
- Change password
- Proper logging instead of prints
- Switch to a SQLite database
- Add colored UI (rich library)

---

## License

MIT License. Free to use and modify.
