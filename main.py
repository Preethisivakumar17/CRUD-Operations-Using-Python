def menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Student")
        name = input("Enter student name: ")
        age = input("Enter age: ")
        department = input("Enter department: ")

        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{department}\n")
        print("Student added successfully!")

    elif choice == "2":
        print("View Students")
        with open("students.txt", "r") as file:
            data = file.readlines()
        for student in data:
            print(student.strip())

    elif choice == "3":
        print("Search Student")
        search_name = input("Enter student name to search: ")
        found = False
        with open("students.txt", "r") as file:
            for student in file:
                if search_name.lower() in student.lower():
                    print(student.strip())
                    found = True
        if not found:
            print("Student not found")

    elif choice == "4":
        print("Update Student")
        student_name = input("Enter student name to update: ")

        with open("students.txt", "r") as file:
            students = file.readlines()

        updated = False

        with open("students.txt", "w") as file:
            for student in students:
                name, age, department = student.strip().split(",")
                if name.lower() == student_name.lower():
                    new_age = input("Enter new age: ")
                    new_department = input("Enter new department: ")

                    file.write(f"{name},{new_age},{new_department}\n")
                    updated = True
                else:
                    file.write(student)

        if updated:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Delete Student")
        student_name = input("Enter student name to delete: ")
        with open("students.txt", "r") as file:
            students = file.readlines()
        deleted = False
        with open("students.txt", "w") as file:
            for student in students:
                name, age, department = student.strip().split(",")
                if name.lower() == student_name.lower():
                    deleted = True
                    continue
                file.write(student)
        if deleted:
            print("Student deleted successfully!")
        else:  
            print("Student not found!")
    
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice")

