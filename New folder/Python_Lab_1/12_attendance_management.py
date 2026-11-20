# Sample: add a student, mark the student present, then display attendance.

attendance_records = {}

while True:
    print("\nAttendance Management")
    print("1. Add a student")
    print("2. Mark attendance")
    print("3. Display attendance")
    print("4. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter the student name: ").strip()
        if name:
            if name not in attendance_records:
                attendance_records[name] = []
                print("Student added.")
            else:
                print("That student is already listed.")
        else:
            print("Student name cannot be empty.")
    elif choice == "2":
        name = input("Enter the student name: ").strip()
        if name not in attendance_records:
            print("Student not found. Add the student first.")
            continue
        status = input("Enter P for present or A for absent: ").strip().upper()
        if status == "P":
            attendance_records[name].append("Present")
            print("Attendance marked present.")
        elif status == "A":
            attendance_records[name].append("Absent")
            print("Attendance marked absent.")
        else:
            print("Please enter P or A.")
    elif choice == "3":
        if attendance_records:
            for name, records in attendance_records.items():
                print(name + ":", ", ".join(records) if records else "No attendance recorded")
        else:
            print("No students have been added.")
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Please choose an option from 1 to 4.")
