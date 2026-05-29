student={}

while True:         #1
    print('''\n------------------------------------------
|       S T U D E N T  M A N A G E R      |
------------------------------------------''')
    print("1.add student")
    print("2.view student")
    print("3.delete student")
    print("4.check result")
    print("5.exit")

    choice= (input("enter your choice: "))

    # add student
    if choice == "1":
        name =input("Enter student name : ")
        marks = int(input("Enter student marks : "))
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
        name = input("Enter student name to delete : ")
        if name in student:
            del student[name]
            print(f"Student {name} deleted successfully.")
        else:
            print(f"Student {name} not found.")

    # check student
    elif choice == "4":
        name = input("enter student name to check :")
        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"{name} : Pass")
            else:
                print(f"{name} : Fail")

        else:
            print(f"student {name} not found.")

    # exit
    elif choice == "5":
        print("\nExiting the program....") 
        print('''------------------------------------------
|       G O O D B Y E   D O S T  !        |
------------------------------------------''')
        break                                       #Loop will break and program will exit
    else:
        print("Invalid choice. Please try again.")














 