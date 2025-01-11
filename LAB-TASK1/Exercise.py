
# Task 1: Introduction
print("Welcome to the Task List Manager!")
print("This program helps you manage your tasks effectively.\n")

# Task 2: Terminal (Simulation of task display in terminal)
def display_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks available.")
    
# Task 3: Python Interpreter (Using Python interpreter for various operations)
# Let's use basic functionality like adding, removing, and listing tasks

# Task 4: Variables
tasks = []  # Initialize an empty list for tasks

# Task 5: Text Editor (Interaction with user to add a task)
def add_task(task_name):
    tasks.append(task_name)
    print(f"Task '{task_name}' added to the list.")

# Task 6: Functions (Creating functions to add, remove, and list tasks)
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed}' removed from the list.")
    else:
        print("Invalid task number. Please try again.")

# Task 7: Lists and Tuples (We are using lists for storing tasks)
# Tuples could be used for storing task properties like (task_name, due_date)

# Task 8: Conditional Statements (Checking if task list is empty)
def check_task_list():
    if not tasks:
        print("You have no tasks to manage. Please add some.")
    else:
        print("You have tasks to manage.")

# Task 9: The For Loop (Iterating over the list of tasks)
def list_all_tasks():
    print("\nListing all tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

# Task 10: User Input and the While Loop (Loop to keep interacting with the user)
def main():
    while True:
        print("\nSelect an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Check if Tasks Exist")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == "2":
            list_all_tasks()
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            check_task_list()
        elif choice == "5":
            print("Exiting Task List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
main()
