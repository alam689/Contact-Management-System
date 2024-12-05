import csv
from contact import Contact

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_contacts(self, contacts):
        try:
            with open(self.file_name, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email", "Address"])
                for contact in contacts:
                    writer.writerow([contact.name, contact.phone, contact.email, contact.address])
                print(f"Contacts saved successfully to {self.file_name}.")
        except Exception as e:
            print(f"Error saving contacts: {e}")

    def load_contacts(self):
        contacts = []
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contacts.append(Contact(row["Name"], row["Phone"], row["Email"], row["Address"]))
        except FileNotFoundError:
            print(f"{self.file_name} not found. A new file will be created upon saving.")
        except Exception as e:
            print(f"Error loading contacts: {e}")
        return contacts
