import datetime
import os
import getpass
import schedule
import time
import subprocess

# Data Storage (Simple Dictionary for Demo; Consider Database for Large Scale)
todo_data = {}

def display_menu():
    print("\n--- DueToday Menu ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Check Due Today")
    print("6. Exit")

def add_task():
    task_name = input("Enter Task Name: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    todo_data[task_name] = due_date
    print(f"Task '{task_name}' added successfully!")

def view_all_tasks():
    if not todo_data:
        print("No tasks available.")
    else:
        for task, due_date in todo_data.items():
            print(f"Task: {task}, Due Date: {due_date}")

def update_task():
    task_name = input("Enter Task Name to Update: ")
    if task_name in todo_data:
        new_due_date = input("Enter New Due Date (YYYY-MM-DD): ")
        todo_data[task_name] = new_due_date
        print(f"Task '{task_name}' updated successfully!")
    else:
        print("Task not found.")

def delete_task():
    task_name = input("Enter Task Name to Delete: ")
    if task_name in todo_data:
        del todo_data[task_name]
        print(f"Task '{task_name}' deleted successfully!")
    else:
        print("Task not found.")

def check_due_today():
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    due_tasks = [task for task, due_date in todo_data.items() if due_date == today]
    if due_tasks:
        print(f"Tasks Due Today ({today}):")
        for task in due_tasks:
            print(task)
        # Simple Notification (Linux/Mac); Modify for Windows
        subprocess.Popen(['notify-send', '-t', '3000', "DueToday Reminder", f"Check your tasks for today!"])
    else:
        print("No tasks due today.")

def job():
    check_due_today()

# Schedule the check_due_today function to run once every day at 8am
schedule.every().day.at("08:00").do(job) # Adjust time as needed

def main():
    print("Welcome to DueToday!")
    while True:
        display_menu()
        choice = input("Choose an Option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            check_due_today()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        
        # Run pending schedule tasks
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
