# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Branch": branch
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found\n")
    else:
        print("\nStudent List:")
        for s in students:
            print("Name:", s["Name"])
            print("Roll:", s["Roll"])
            print("Branch:", s["Branch"])
            print("-----------------")


def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["Roll"] == roll:
            print("Student Found")
            print("Name:", s["Name"])
            print("Branch:", s["Branch"])
            return

    print("Student not found\n")


def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Student deleted successfully\n")
            return

    print("Student not found\n")


while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program exited")
        break
    else:
        print("Invalid choice\n")