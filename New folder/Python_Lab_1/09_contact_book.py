# Sample: use the menu to add, search, display, or delete a name and phone number.

contacts = {}

while True:
    print("\nContact Book")
    print("1. Add or update a contact")
    print("2. Search for a contact")
    print("3. Display all contacts")
    print("4. Delete a contact")
    print("5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter the contact name: ").strip()
        phone = input("Enter the phone number: ").strip()
        if name and phone:
            contacts[name] = phone
            print("Contact saved.")
        else:
            print("Name and phone number cannot be empty.")
    elif choice == "2":
        name = input("Enter the name to search: ").strip()
        if name in contacts:
            print(name + ":", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "3":
        if contacts:
            for name, phone in contacts.items():
                print(name + ":", phone)
        else:
            print("The contact book is empty.")
    elif choice == "4":
        name = input("Enter the name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "5":
        print("Goodbye.")
        break
    else:
        print("Please choose an option from 1 to 5.")
