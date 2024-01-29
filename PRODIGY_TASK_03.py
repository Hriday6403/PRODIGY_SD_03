import json

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def edit_contact(self, name, new_phone, new_email):
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone
            self.contacts[name]['email'] = new_email
            print(f"Contact for {name} updated successfully.")
        else:
            print(f"Contact for {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print(f"Contact for {name} not found.")

    def save_contacts_to_file(self, filename='contacts.json'):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print("Contacts saved to file successfully.")

    def load_contacts_from_file(self, filename='contacts.json'):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print("Contacts loaded from file successfully.")
        except FileNotFoundError:
            print("No previous contacts found.")

if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            name = input("Enter name of the contact to edit: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            contact_manager.edit_contact(name, new_phone, new_email)
        elif choice == '4':
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            contact_manager.save_contacts_to_file()
        elif choice == '6':
            contact_manager.load_contacts_from_file()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
