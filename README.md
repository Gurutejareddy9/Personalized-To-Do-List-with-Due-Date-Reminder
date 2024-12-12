# DueToday - Personalized To-Do List with Due Date Reminders

A simple Python application to manage your daily tasks with due date reminders.

## Features
- **CRUD Operations**: Create, Read, Update, Delete tasks easily.
- **Due Date Reminders**: Receive reminders for tasks due today (configurable timing).
- **Simple & Secure**: No external dependencies for storage; uses a local dictionary for demo purposes.

## Getting Started
1. Clone the repository: `git clone https://github.com/Gurutejareddy9/DueToday.git`
2. Navigate into the project directory: `cd DueToday`
3. Run the application: `python due_today.py`

## Usage
- **Add Task**: Enter task name and due date (YYYY-MM-DD) when prompted.
- **View Tasks**: Lists all tasks with their due dates.
- **Update/Delete Task**: Find tasks by their names.
- **Check Due Today**: Manually check for due tasks or rely on scheduled reminders.

## Customization
- **Reminder Timing**: Modify the `schedule.every().day.at("08:00").do(job)` line in `due_today.py` to change the reminder time.
- **Notification System**: The current notification system uses `notify-send` (Linux/Mac)
