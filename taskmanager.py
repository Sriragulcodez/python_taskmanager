from collections import deque

stack_task=[]
queue_task=deque()
completed_tasks=[]

def add_task_stack(task_name , task_type):
    if task_type.lower() == "stack":
        stack_task.append(task_name)
        print(f"Task '{task_name}' added to stack.")
        
    elif task_type.lower() == "queue":
        queue_task.append(task_name)
        print(f"Task '{task_name}' added to queue.")

    else:
      return "Invalid task type"

def view_tasks(task_type):
    if task_type.lower() == "stack":
        if stack_task:
            print("Stack Tasks:")
            for task in reversed(stack_task):
                print(f"- {task}")
        else :
            print("No tasks in stack.")

    if task_type.lower() == "queue":
        if queue_task:
            print("Queue Tasks:")
            for task in queue_task:
                print(f"- {task}")
        else :
            print("No tasks in queue.")

def remove_task(task_type):
    if task_type.lower() == "stack":
        if stack_task:
            completed_task = stack_task.pop()
            completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' removed from stack and marked as completed.")
        else:
            print("No tasks in stack to remove.")

    elif task_type.lower() == "queue":
        if queue_task:
            completed_task = queue_task.popleft()
            completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' removed from queue and marked as completed.")
        else:
            print("No tasks in queue to remove.")

    else:
      return "Invalid task type"
    
def search_task(task_name):
    found_in_stack = task_name in stack_task
    found_in_queue = task_name in queue_task

    if found_in_stack:
        print(f"Task '{task_name}' found in stack.")
    if found_in_queue:
        print(f"Task '{task_name}' found in queue.")
    if not (found_in_stack or found_in_queue):
        print(f"Task '{task_name}' not found in stack or queue.")

def sort_tasks(task_type):
    if task_type.lower() == "stack":
        stack_task.sort()
        print("Stack tasks sorted alphabetically.")

    elif task_type.lower() == "queue":
        queue_task = deque(sorted(queue_task))
        print("Queue tasks sorted alphabetically.")

    else:
      return "Invalid task type"

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Search Task")
        print("5. Sort Tasks")
        print("6. View Completed Tasks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            task_type = input("Enter task type (stack/queue): ")
            add_task_stack(task_name, task_type)

        elif choice == '2':
            task_type = input("Enter task type to view (stack/queue): ")
            view_tasks(task_type)

        elif choice == '3':
            task_type = input("Enter task type to remove from (stack/queue): ")
            remove_task(task_type)

        elif choice == '4':
            task_name = input("Enter task name to search: ")
            search_task(task_name)

        elif choice == '5':
            task_type = input("Enter task type to sort (stack/queue): ")
            sort_tasks(task_type)

        elif choice == '6':
            if completed_tasks:
                print("Completed Tasks:")
                for task in completed_tasks:
                    print(f"- {task}")
            else:
                print("No completed tasks.")

        elif choice == '7':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()