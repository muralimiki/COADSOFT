from contact import Contact
from storage import Storage

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
            return
        print("\n===== CONTACT LIST =====")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        found = False
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = Contact(name, phone, email, address)
            self.save_contacts()
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted = self.contacts.pop(index)
            self.save_contacts()
            print(f"Deleted contact: {deleted.name}")
        else:
            print("Invalid contact number.")

    def save_contacts(self):
        Storage.save(self.contacts)
    def load_contacts(self):
        data = Storage.load()
        self.contacts = [Contact.from_dict(item) for item in data]