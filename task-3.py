'''Task-03
Implement a Simple Contact Management System
Develop a program that allows users to store and manage contact information.
The program should provide options to add a new contact by entering their name
, phone number, and email address. It should also allow users to view their contact list, 
edit existing contacts, and delete contacts if needed. The program should store the contacts 
in memory or in a file for persistent storage.
'''
import os

FILE_NAME = "contacts.txt"

# Ensure file exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass  # create empty file

# Read contacts from file
def load_contacts():
    contacts = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone, email = line.strip().split("|")
            contacts.append([name, phone, email])
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write("|".join(contact) + "\n")

# Add new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + phone + "|" + email + "\n")

    print("Contact added successfully!\n")

# View contacts
def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    print()

# Edit contact
def edit_contact():
    contacts = load_contacts()
    view_contacts()

    if not contacts:
        return

    try:
        choice = int(input("Enter contact number to edit: ")) - 1
        if 0 <= choice < len(contacts):
            print("Leave blank to keep old value.")

            name = input("New Name: ")
            phone = input("New Phone: ")
            email = input("New Email: ")

            if name:
                contacts[choice][0] = name
            if phone:
                contacts[choice][1] = phone
            if email:
                contacts[choice][2] = email

            save_contacts(contacts)
            print("Contact updated successfully!\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Delete contact
def delete_contact():
    contacts = load_contacts()
    view_contacts()

    if not contacts:
        return

    try:
        choice = int(input("Enter contact number to delete: ")) - 1
        if 0 <= choice < len(contacts):
            removed = contacts.pop(choice)
            save_contacts(contacts)
            print(f"Contact '{removed[0]}' deleted successfully!\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main menu
def main():
    initialize_file()

    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()