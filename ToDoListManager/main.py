# main.py

from todo_list import TodoListManager

def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Clear all tasks")
    print("6. Exit")

def printTasks(tasks):
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks found.")
        
def main():
    manager = TodoListManager()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task_name = input("Enter the task name: ").strip().lower()
            manager.add_task(task_name)
            print(f"Task '{task_name}' added.")
        
        elif choice == "2":
            tasks = manager.list_tasks()
            printTasks(tasks)
        
        elif choice == "3":
            print("Enter one of the next task name to mark as completed: ")
            printTasks(manager.list_tasks())
            task_name = input().strip()

            manager.mark_task_completed(task_name)
            print(f"Task '{task_name}' marked as completed.")
        
        elif choice == "4":
            print("Enter one of the next task name to delete it: ")
            printTasks(manager.list_tasks())
            task_name = input().strip()
            manager.delete_task(task_name.lower())
            print(f"Task '{task_name}' delete it.")
            
        elif choice == "5":
            manager.clear_tasks()
            print("All tasks cleared.")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
