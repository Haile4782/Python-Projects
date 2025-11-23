def todo_app():
    tasks = [] # List to store task dictionaries
    
    print("To-Do List Manager")
    
    while True:
        print("\nMenu: [1] Add  [2] View  [3] Complete  [4] Delete  [5] Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            # Add Task
            task_name = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            tasks.append({"task": task_name, "priority": priority, "done": False})
            print("Task added.")
            
        elif choice == '2':
            # View List
            print("\nCurrent Tasks:")
            for i, t in enumerate(tasks):
                status = "[x]" if t['done'] else "[ ]"
                print(f"{i+1}. {status} {t['task']} (Priority: {t['priority']})")
                
        elif choice == '3':
            # Mark Complete
            try:
                idx = int(input("Enter task number to mark complete: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]['done'] = True
                    print("Task marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            # Delete
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    print(f"Removed: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '5':
            # Exit and Summary
            completed_count = sum(1 for t in tasks if t['done'])
            pending_count = len(tasks) - completed_count
            print("\n--- Summary ---")
            print(f"Completed Tasks: {completed_count}")
            print(f"Pending Tasks:   {pending_count}")
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run the program
todo_app()