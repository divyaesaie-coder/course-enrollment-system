#Program to manage student course enrollment, seat allocation and student records.
python_seats = 5
java_seats = 3

enrolled_python = []
enrolled_java = []

while True:
    print("\n1) Enroll student")
    print("2) Drop student")
    print("3) View roster")
    print("4) Exit")

    ch = input("Choose: ")

    # ENROLL
    if ch == "1":
        name = input("Enter student name: ")
        course = input("Enter course (python/java): ").lower()

        if course == "python":
            if name in enrolled_python:
                print("Student already enrolled in Python")
            elif python_seats == 0:
                print("Python course is full")
            else:
                enrolled_python.append(name)
                python_seats -= 1
                print("Enrolled in Python")

        elif course == "java":
            if name in enrolled_java:
                print("Student already enrolled in Java")
            elif java_seats == 0:
                print("Java course is full")
            else:
                enrolled_java.append(name)
                java_seats -= 1
                print("Enrolled in Java")
        else:
            print("Invalid course")

    # DROP
    elif ch == "2":
        name = input("Enter student name: ")
        course = input("Enter course (python/java): ").lower()

        if course == "python":
            if name in enrolled_python:
                enrolled_python.remove(name)
                python_seats += 1
                print("Dropped from Python")
            else:
                print("Student not found in Python")

        elif course == "java":
            if name in enrolled_java:
                enrolled_java.remove(name)
                java_seats += 1
                print("Dropped from Java")
            else:
                print("Student not found in Java")
        else:
            print("Invalid course")

    # VIEW ROSTER
    elif ch == "3":
        print("\nPython Course")
        print("Seats left:", python_seats)
        print("Students:", enrolled_python)

        print("\nJava Course")
        print("Seats left:", java_seats)
        print("Students:", enrolled_java)

    # EXIT
    elif ch == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")

