age = int(input("Enter age:"))
if age>=18:
    ticket=input("do you have a ticket? (yes/no): ")
    if ticket=="yes":
        print("you can enter ")
    else:
        print("you cannot enter")
else:
    print("you cannot enter")