tasks = []
while True:
    print("\n1.Enter new task")
    print("\n2.Delete task")
    print("\n3.view all task")
    print("\n4.Exit")
    choice = int(input("\nEnter your choice here: "))

    if choice == 1:
        task = input("\nEnter task: ")
        tasks.append(task)
        print("\nTask added successfully")
    elif choice == 2:
        if len(tasks) == 0:
            print("\nNo task to delete")
        else:
            taskk = input("Enter the task to delete: ")
            if taskk in tasks:
                tasks.remove(taskk)
                print("task removed successfully")
    elif choice == 3:
        if len(tasks) == 0:
            print("No task to show")
        else:
            print("\nShowing all tasks:")
            for i in tasks:
                print("\n" + i)
    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("\nPlease enter a valid choice")

