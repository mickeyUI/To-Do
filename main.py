from storage import load_task, save_task, complete, delete_task
from task import Tasks
while True:
    Tasks.to_list(load_task())
    print("\n--- MAIN MENU ---")
    print("""
        1. Add Task
        2. Complete Task
        3. Delete Task
        4. Exit""")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("What task do you want to add")
        task = input(": ")
        save_task(task)

    elif choice == '2':
        print("what task do you want to mark complete")
        com_task = input(": ")
        complete(com_task)
    elif choice == '3':
        print("which task do you want to delete")
        del_task = input(": ")
        delete_task(del_task)
    elif choice == '4':
        print("Goodbye!")
        break  
    else:
        print("Invalid choice, please try again.")




