# Contact Book in Python

This is a simple command-line Contact Book application implemented in Python. It allows you to store, view, search, update, and delete contact information.

## Features

- **Contact Information**: Store name, phone number, email, and address for each contact.
- **Add Contact**: Allow users to add new contacts with their details.
- **View Contact List**: Display a list of all saved contacts with names and phone numbers.
- **Search Contact**: Implement a search function to find contacts by name or phone number.
- **Update Contact**: Enable users to update contact details.
- **Delete Contact**: Provide an option to delete a contact.
- **User Interface**: Designed to be user-friendly for easy interaction.

## Requirements

- Python 3.x

## How to Run

1. **Clone the Repository:**

    ```sh
    git clone git@github.com:YourUsername/Contact-Book-Python.git
    cd Contact-Book-Python
    ```

2. **Run the Script:**

    ```sh
    python contact_book.py
    ```

## How to Use

1. **Add Contact**: Choose option 1 and enter the contact details.
2. **View Contact List**: Choose option 2 to see all saved contacts.
3. **Search Contact**: Choose option 3 and enter the name or phone number to search.
4. **Update Contact**: Choose option 4 and enter the name of the contact to update. Then enter the new details.
5. **Delete Contact**: Choose option 5 and enter the name of the contact to delete.
6. **Exit**: Choose option 6 to exit the application.

## Example Interaction

Contact Book Menu:

    1. Add Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    Enter your choice (1-6): 1
    Enter name: John Doe
    Enter phone number: 1234567890
    Enter email: john@example.com
    Enter address: 123 Elm Street
    Contact added successfully!

Contact Book Menu:

    1. Add Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    Enter your choice (1-6): 2

Contact List:

    John Doe - 1234567890

Contact Book Menu:

    1. Add Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    Enter your choice (1-6): 3
    Enter name or phone number to search: John

Search Results:
John Doe, 1234567890, john@example.com, 123 Elm Street

Contact Book Menu:

    1. Add Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    Enter your choice (1-6): 4
    Enter the name of the contact to update: John Doe
    Enter new phone number: 0987654321
    Enter new email: john.doe@example.com
    Enter new address: 456 Oak Street
    Contact updated successfully!

Contact Book Menu:

    1. Add Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    Enter your choice (1-6): 5
    Enter the name of the contact to delete: John Doe
    Contact deleted successfully!

Contact Book Menu:

    1. Add Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit
    Enter your choice (1-6): 6
    Exiting Contact Book. Goodbye!


## Code Structure

- `Contact`: Class to store individual contact details.
- `ContactBook`: Class to manage the list of contacts and provide functionality to add, view, search, update, and delete contacts.
- `menu`: Function to provide a user-friendly interface for interacting with the contact book.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

This README file provides a comprehensive guide on how to use the Contact Book project, including features, requirements, how to run, and an example interaction.
