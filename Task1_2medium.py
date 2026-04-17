file = "tasks.txt"

# View tasks
def view_tasks():
    try:
        f = open(file, "r")
        tasks = f.readlines()
        f.close()

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i].strip())
    except:
        print("File not found.")

# Add task
def add_task():
    task = input("Enter new task: ")
    f = open(file, "a")
    f.write(task + "\n")
    f.close()
    print("Task added!")

# Edit task
def edit_task():
    f = open(file, "r")
    tasks = f.readlines()
    f.close()

    view_tasks()
    n = int(input("Enter task number to edit: "))
    new_task = input("Enter new task: ")
    tasks[n-1] = new_task + "\n"

    f = open(file, "w")
    f.writelines(tasks)
    f.close()
    print("Task updated!")

# Delete task
def delete_task():
    f = open(file, "r")
    tasks = f.readlines()
    f.close()

    view_tasks()
    n = int(input("Enter task number to delete: "))
    tasks.pop(n-1)

    f = open(file, "w")
    f.writelines(tasks)
    f.close()
    print("Task deleted!")

# Menu
while True:
    print("\n--- TO DO APPLICATION ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        view_tasks()
    elif ch == "3":
        edit_task()
    elif ch == "4":
        delete_task()
    elif ch == "5":
        break
    else:
        print("Invalid choice")