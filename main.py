import os
import json
import time 
import getpass
user_file = 'user.json'
task_file = 'user_tasks.json'
current_user = None
tasks = []

def clear_terminal():
    os.system('cls' if os.name =='nt' else 'clear')
def countdown(t):
    for i in range(t,0,-1):
        print(i)
        time.sleep(1)

def welcome():
    print("\n------Welcome to to-do app-------\n")
    print("1.Sign Up\n2.Log In")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        clear_terminal()
        sign_up()
    elif choice == 2:
        clear_terminal()
        log_in()
    else:
        print("Invalid choice")
        


def load_users():
    if os.path.exists(user_file):
        with open(user_file,'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = [] 
    else:
        users = []
    return users

def save_users(users):
    with open(user_file, 'w') as f:
        json.dump(users,f,indent=4)

def get_username():
    while True:
        name = input("Enter your username: ").strip()
        if name:
            return name.capitalize()
        else:
            print("Username cannot be empty. Please try again.")
def get_password():
    while True:
        password = getpass.getpass("Enter you password: ").strip()
        if password:
            return password
        else:
            print("Password cannot be empty. Please try again.")
def username_exists(name,users):
    return any(i['name']==name for i in users)

def sign_up():
    print("\n------Sign up into to-do app-------\n")
    
    users = load_users()
    while True:

        name = get_username()
        if username_exists(name,users):
            print("------User with this username already exists------\n")
            print("Please choose a different username.")
            print('1.Try again\n2.Log in')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                continue
            elif choice == 2:
                clear_terminal()
                log_in()
                return
            else:
                print("Invalid choice. Please try again.")
                continue 
        password = get_password()

        user = {
        'name': name,
        'password': password
        }
    
    
        users.append(user)
        save_users(users)   
        print('------Sign up Successful-------')
        print('------Returning to login page in -------')
        countdown(3)
        clear_terminal()
        log_in()

def log_in():
    print("\n------Log-in into to-do app-------\n")
    users = load_users()

    while True:
        global current_user
        name = get_username()
        password = get_password()
        for user in users:
            if user['name'] == name and user['password'] == password:
                print('Login Successful')
                current_user = user['name']
                print('------Redirecting to dashboard in -------')
            
                countdown(3)
                clear_terminal()
                dashboard()
                break
        else:
            print('Invalid credentials\n')
            print('------Try again in -------')
            countdown(3)
            clear_terminal()
            continue

def dashboard():
    print(f"\n------Welcome {current_user}, to your dashboard-------\n")
    print("1. View tasks\n2. Add task\n3.Logout")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        clear_terminal()
        view_tasks()
    elif choice == 2:
        clear_terminal()
        add_task()
    elif choice == 3:
        print("Logging out...")
        time.sleep(1)
        print
        clear_terminal()
        welcome()
    else:
        print("Invalid choice")
        dashboard()


def view_tasks():
    
    with open(task_file, 'r') as f:
        existing_tasks = json.load(f)
    user_tasks = existing_tasks.get(current_user,[])
    if not user_tasks:
        print(f"------No tasks found for {current_user}------\n")
        print('-----Redirecting to dashboard-------\n')
        countdown(3)
        clear_terminal()
        dashboard()
    else:
        print(f"\n------Tasks for {current_user}-------\n")
    for task in user_tasks:
        print(f"ID: {task['id']}\nTime: {task['time']}\nTask: {task['task_name']}\nStatus: {task['status']}\n")
    print('-----End of tasks-------\n')
    print(f'Enter ''ID'' to mark task as completed or enter 0 to go to dashboard')
    choice = int(input("Enter your choice: "))
    if choice == 0:
        clear_terminal()
        dashboard()
    else:
        for task in user_tasks:
            if task['id'] == choice:
                task['status'] = 'completed'
                print(f"\n-----Task ID '{choice}' : '{task['task_name']}' marked as completed!-----\n")
                break
        else:
            print("Invalid task ID")
        with open (task_file, 'w') as f:
            json.dump(existing_tasks, f, indent=4)
        time.sleep(1)
        print('-----What do you want to do next?------\n')
        time.sleep(1)
        print('1. View tasks again\n2. Go to dashboard')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            clear_terminal()
            view_tasks()
        elif choice == 2:
            clear_terminal()
            dashboard()
        else:
            print("Invalid choice")
    
def add_task():
    print("\n------Add Task-------\n")
    timet = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    t_name = input('Enter your task: ')
    status = 'pending'
    task = {
        'id':None,
        'time': timet,
        'task_name': t_name,
        'status': status
    }

    if os.path.exists(task_file):
        with open(task_file,'r') as f:
            try:
                existing_tasks = json.load(f)
            except json.JSONDecodeError:
                existing_tasks = {} 
    else:
        existing_tasks = {}

    if current_user not in existing_tasks:
        existing_tasks[current_user] = []
    m_id = max([t['id'] for t in existing_tasks[current_user]], default=0)
    task['id'] = m_id + 1

    existing_tasks[current_user].append(task)

    with open (task_file, 'w') as f:
        json.dump(existing_tasks, f, indent=4)
    print(f"\n-----Task '{t_name}' added successfully for user '{current_user}'!-----\n")
    time.sleep(1)
    print('-----What do you want to do next?------\n')

    time.sleep(1)
    print('1. Add another task\n2. Go to dashboard')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        clear_terminal()
        add_task()
    elif choice == 2:
        clear_terminal()
        dashboard()
    else:
        print("Invalid choice")
    
welcome()
