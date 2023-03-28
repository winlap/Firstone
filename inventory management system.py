open("inventory.txt","w")
#function to display all the item in the file
def display_items():
    with open("inventory.txt","r") as f:
        for line in f:
            print(line.strip())

#functin to delete an item in the file
def delete_item():
    item_to_delete = input("\nEnter the item you want to delete")
    with open("inventory.txt","r") as f:
        lines = f.readlines()
    with open("inventory.txt","w") as f:
        for line in lines:
            if line.strip() != item_to_delete:
                f.write(line)
    print("\nItem deleted successfully")

#function to add an item in the file
def add_item():
    item = input("\nEnter the item to add: ")
    with open("inventory.txt","a+") as f:
        f.write(item + "\n")
    print("\nItem added successfully")

#main loop
while True:
    print("\n1.Add item to the inventory")
    print("\n2.List of all items")
    print("\n3.Delete item")
    print("\n4.Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        display_items()
    elif choice == 3:
        delete_item()
    elif choice == 4:
        break
    else:
        print("\nPlease enter valid option")


