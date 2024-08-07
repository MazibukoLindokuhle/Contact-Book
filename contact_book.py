class Contact:
    def __init__(self, name, phone, email, address):
        # Initialize the contact with the given details
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        # String representation of the contact
        return f"{self.name}, {self.phone}, {self.email}, {self.address}"


class ContactBook:
    def __init__(self):
        # Initialize an empty contact list
        self.contacts = []

    def add_contact(self, contact):
        # Add a new contact to the contact list
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        # Display all contacts in the contact list
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        # Search for contacts by name or phone number
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not results:
            print("No contacts found.")
            return
        print("\nSearch Results:")
        for contact in results:
            print(contact)

    def update_contact(self, name):
        # Update details of a contact identified by name
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        # Delete a contact identified by name
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

    def menu(self):
        # Display the menu and handle user interaction
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                # Add a new contact
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                contact = Contact(name, phone, email, address)
                self.add_contact(contact)
            elif choice == '2':
                # View the contact list
                self.view_contacts()
            elif choice == '3':
                # Search for a contact
                keyword = input("Enter name or phone number to search: ")
                self.search_contact(keyword)
            elif choice == '4':
                # Update a contact's details
                name = input("Enter the name of the contact to update: ")
                self.update_contact(name)
            elif choice == '5':
                # Delete a contact
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                # Exit the application
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    # Create an instance of ContactBook and display the menu
    contact_book = ContactBook()
    contact_book.menu()
