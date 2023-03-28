import os

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(6):
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    with open("student_records.txt", "a") as file:
        file.write(f"{name}:{','.join(map(str, marks))}\n")
    print("Student added successfully.")

def view_students():
    with open("student_records.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.")
        else:
            for record in records:
                name, marks_str = record.strip().split(":")
                marks = list(map(float, marks_str.split(",")))
                print(f"{name}: {marks}")

def edit_student():
    name = input("Enter student name to edit: ")
    with open("student_records.txt", "r") as file:
        records = file.readlines()
    found = False
    with open("student_records.txt", "w") as file:
        for record in records:
            record_name, marks_str = record.strip().split(":")
            if record_name == name:
                found = True
                marks = []
                for i in range(6):
                    mark = float(input(f"Enter new mark {i+1}: "))
                    marks.append(mark)
                file.write(f"{name}:{','.join(map(str, marks))}\n")
                print("Student edited successfully.")
            else:
                file.write(record)
    if not found:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    with open("student_records.txt", "r") as file:
        records = file.readlines()
    found = False
    with open("student_records.txt", "w") as file:
        for record in records:
            record_name, marks_str = record.strip().split(":")
            if record_name == name:
                found = True
                print(f"{name}: {marks_str} deleted successfully.")
            else:
                file.write(record)
    if not found:
        print("Student not found.")

def main():
    while True:
        print("\nWhat would you like to do?\n1. Add student\n2. View students\n3. Edit student\n4. Delete student\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    print("Exiting program.")

if not os.path.exists("student_records.txt"):
    open("student_records.txt", "w").close()

main()
