# Program 6: Dynamic Phonebook and Contact Directory Manager

contacts = {}

while True:
    print("\n===== PHONEBOOK MENU =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully.")

    # Search Contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")

    # Update Contact
    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Display All Contacts
    elif choice == "5":
        if len(contacts) == 0:
            print("Phonebook is empty.")
        else:
            print("\n===== ALL CONTACTS =====")
            for name, phone in contacts.items():
                print(name, ":", phone)

    # Exit
    elif choice == "6":
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice. Please try again.")