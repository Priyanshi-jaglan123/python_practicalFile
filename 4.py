import heapq

# Priority queue
tasks = []


# Generator for lazy task evaluation
def task_generator():
    while tasks:
        priority, task = heapq.heappop(tasks)
        yield priority, task


def add_task():
    task = input("Enter task: ")
    priority = int(input("Enter priority (1 = highest): "))

    heapq.heappush(tasks, (priority, task))
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for priority, task in sorted(tasks):
        print(f"Priority: {priority} | Task: {task}")


def execute_task():
    if not tasks:
        print("No tasks to execute.")
        return

    # Lazy evaluation
    generator = task_generator()

    priority, task = next(generator)

    print(f"\nExecuting task: {task}")
    print(f"Priority: {priority}")


# Interactive command-line interface
while True:

    print("\n===== TASK SCHEDULER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Execute Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        execute_task()

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice. Try again.")
        