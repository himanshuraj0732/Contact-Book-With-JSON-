import json
import os

# File name for storing contacts
FILE_NAME = "contacts.json"

# Load contacts from JSON file (if it exists)
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

# Save contacts to JSON file
def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

# Initialize contacts from file
contacts = load_contacts()

def add_contacts(name, phone):
    if name in contacts:
        print(f"{name} already exists with number {contacts[name]}")
    else:
        contacts[name] = phone
        save_contacts()
        print(f"Contact {name} added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Name not found in contacts.")

def delete_contacts(name):
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("The contact is deleted successfully.")
    else:
        print("The name is not found in contacts.")

def menu():
    while True:
        print("\n--------- Contacts Book ----------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Exit")
        print("---------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the number: ")
            add_contacts(name, phone)

        elif choice == "2":
            name = input("Enter the name: ")
            search_contact(name)

        elif choice == "3":
            name = input("Enter the name: ")
            delete_contacts(name)

        elif choice == "4":
            print("Exiting.....")
            break

        else:
            print("Invalid choice! Please try again.")

menu()
