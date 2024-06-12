import re

# Nested dictionary to store contact information
contacts = {}

def display_menu():
    """Displays the main menu options."""
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def validate_input(pattern, prompt):
    """Validates user input based on the given regex pattern."""
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def add_contact():
    """Adds a new contact to the system."""
    unique_id = validate_input(r"^\S+@\S+\.\S+$", "Enter unique identifier (email): ")
    name = input("Enter name: ")
    phone = validate_input(r"^\+?\d{10,15}$", "Enter phone number: ")
    email = validate_input(r"^\S+@\S+\.\S+$", "Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")
    contacts[unique_id] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact added successfully!")

def edit_contact():
    """Edits an existing contact's information."""
    unique_id = validate_input(r"^\S+@\S+\.\S+$", "Enter unique identifier of the contact to edit: ")
    if unique_id in contacts:
        name = input("Enter new name: ")
        phone = validate_input(r"^\+?\d{10,15}$", "Enter new phone number: ")
        email = validate_input(r"^\S+@\S+\.\S+$", "Enter new email address: ")
        additional_info = input("Enter new additional information (address, notes): ")
        contacts[unique_id] = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Additional Info": additional_info
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    """Deletes a contact from the system."""
    unique_id = validate_input(r"^\S+@\S+\.\S+$", "Enter unique identifier of the contact to delete: ")
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    """Searches for a contact by unique identifier and displays their details."""
    unique_id = validate_input(r"^\S+@\S+\.\S+$", "Enter unique identifier of the contact to search: ")
    if unique_id in contacts:
        contact = contacts[unique_id]
        print(f"ID: {unique_id}")
        print("Name:", contact["Name"])
        print("Phone:", contact["Phone"])
        print("Email:", contact["Email"])
        print("Additional Info:", contact["Additional Info"])
    else:
        print("Contact not found!")

def display_all_contacts():
    """Displays all contacts in the system."""
    if contacts:
        for unique_id, contact in contacts.items():
            print(f"ID: {unique_id}")
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("Additional Info:", contact["Additional Info"])
            print("-" * 20)
    else:
        print("No contacts found!")

def export_contacts():
    """Exports contacts to a text file."""
    with open("contacts.txt", "w") as file:
        for unique_id, contact in contacts.items():
            file.write(f"{unique_id},{contact['Name']},{contact['Phone']},{contact['Email']},{contact['Additional Info']}\n")
    print("Contacts exported successfully!")

def import_contacts():
    """Imports contacts from a text file."""
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                unique_id, name, phone, email, additional_info = line.strip().split(',')
                contacts[unique_id] = {
                    "Name": name,
                    "Phone": phone,
                    "Email": email,
                    "Additional Info": additional_info
                }
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("File not found!")

def main():
    """Main function to run the Contact Management System."""
    while True:
        try:
            display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                add_contact()
            elif choice == '2':
                edit_contact()
            elif choice == '3':
                delete_contact()
            elif choice == '4':
                search_contact()
            elif choice == '5':
                display_all_contacts()
            elif choice == '6':
                export_contacts()
            elif choice == '7':
                import_contacts()
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Returning to the main menu...")

if __name__ == "__main__":
    main()
