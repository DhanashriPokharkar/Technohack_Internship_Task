tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)
        print()

while True:
    print("----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
