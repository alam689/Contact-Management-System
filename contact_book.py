class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if any(c.phone == contact.phone for c in self.contacts):
            print("Duplicate phone number. Contact not added.")
            return
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        results = [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone or query.lower() in c.email.lower()]
        return results

    def remove_contact(self, phone):
        if any(c.phone == phone for c in self.contacts):
            self.contacts = [c for c in self.contacts if c.phone != phone]
            print("Contact removed successfully.")
        else:
            print("Phone number not found. No contact removed.")
