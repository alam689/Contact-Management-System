from contact_book import ContactBook
from file_manager import FileManager
from contact import Contact
import re

class MenuApp:
    def __init__(self):
        self.contact_book = ContactBook()
        self.file_manager = FileManager("contacts.csv")
        # Load contacts from the file during initialization
        self.contact_book.contacts = self.file_manager.load_contacts()

    def run(self):
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Remove Contact")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.contact_book.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.remove_contact()
            elif choice == '5':
                # Save contacts before exiting
                self.file_manager.save_contacts(self.contact_book.contacts)
                print("Exiting... Contacts saved.")
                break
            else:
                print("Invalid choice. Try again!")

    def add_contact(self):
        name = input("Enter Name: ")
        while not self.validate_name(name):
            print("Invalid name. Must contain only letters, spaces, hyphens, or apostrophes.")
            name = input("Enter Name: ")

        phone = input("Enter Phone: ")
        while not self.validate_phone(phone):
            print("Invalid phone number. Must be numeric and 11 digits.")
            phone = input("Enter Phone: ")

        email = input("Enter Email: ")
        while not self.validate_email(email):
            print("Invalid email. Please enter a valid email address (must contain '@' and '.').")
            email = input("Enter Email: ")

        address = input("Enter Address: ")

        contact = Contact(name, phone, email, address)
        self.contact_book.add_contact(contact)
        # Save contacts after adding
        self.file_manager.save_contacts(self.contact_book.contacts)

    def search_contact(self):
        query = input("Enter name, phone, or email to search: ")
        results = self.contact_book.search_contact(query)
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contact found.")

    def remove_contact(self):
        phone = input("Enter Phone of the contact to remove: ")
        self.contact_book.remove_contact(phone)
        # Save contacts after removing
        self.file_manager.save_contacts(self.contact_book.contacts)

    @staticmethod
    def validate_name(name):
        # Name can contain letters, spaces, hyphens, or apostrophes
        pattern = r"^[A-Za-z\s'-]+$"
        return bool(re.match(pattern, name))

    @staticmethod
    def validate_phone(phone):
        # Phone should be numeric and 11 digits
        return phone.isdigit() and len(phone) == 11

    @staticmethod
    def validate_email(email):
        # Email should contain '@' and '.'
        return "@" in email and "." in email
