student = {}
PASS_THRESHOLD = 40

while True:  # 1
    print(
        "\n------------------------------------------\n"
        "|       S T U D E N T  M A N A G E R      |\n"
        "------------------------------------------"
    )
    print("1.add student")
    print("2.view student")
    print("3.delete student")
    print("4.check result")
    print("5.exit")

    choice = input("enter your choice: ").strip()

    # add student
    if choice == "1":
        name = input("Enter student name : ").strip()

        while True:
            marks_input = input("Enter student marks : ").strip()
            try:
                marks = int(marks_input)
                break
            except ValueError:
                print("Invalid marks. Please enter an integer value.")

        student[name] = marks
        print(f"Student {name} added successfully.")

    # view student
    elif choice == "2":
        if student:
            print("\nstudent name and marks : ")
            for name, marks in student.items():
                print(f"{name} : {marks}")
        else:
            print("No students found.")

    # delete student
    elif choice == "3":
        name = input("Enter student name to delete : ").strip()
        if name in student:
            del student[name]
            print(f"Student {name} deleted successfully.")
        else:
            print(f"Student {name} not found.")

    # check student
    elif choice == "4":
        name = input("enter student name to check :").strip()
        if name in student:
            marks = student[name]
            if marks >= PASS_THRESHOLD:
                print(f"{name} : Pass")
            else:
                print(f"{name} : Fail")
        else:
            print(f"student {name} not found.")

    # exit
    elif choice == "5":
        print("\nExiting the program....")
        print(
            "------------------------------------------\n"
            "|       G O O D B Y E   D O S T  !        |\n"
            "------------------------------------------"
        )
        break  # Loop will break and program will exit

    else:
        print("Invalid choice. Please try again.")

