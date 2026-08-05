student_name = input("Enter your name: ")
usn = input("Enter your USN: ")
branch = input("Enter your branch: ")
semester = int(input("Enter your semester: "))
sub1=int(input("Enter marks for subject 1: "))
sub2=int(input("Enter marks for subject 2: "))  
sub3=int(input("Enter marks for subject 3: "))
print(f"Student name is {student_name} and USN is {usn}")
print(f"Branch is {branch} and semester is {semester}")
print(f"Marks for subject 1 is {sub1}, subject 2 is {sub2} and subject 3 is {sub3}")
total_marks = sub1 + sub2 + sub3
print(f"Total marks obtained is {total_marks}")
avg_marks = total_marks / 3
print(f"Average marks obtained is {avg_marks:.2f}")
    


