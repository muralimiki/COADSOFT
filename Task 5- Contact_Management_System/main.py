from contact_manager import ContactManager

def menu():
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            manager.search_contact(keyword)

        elif choice == '4':
            manager.view_contacts()

            try:
                index = int(input("Enter contact number to update: ")) - 1
                name = input("Enter New Name: ")
                phone = input("Enter New Phone Number: ")
                email = input("Enter New Email: ")
                address = input("Enter New Address: ")
                manager.update_contact(index, name, phone, email, address)
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            manager.view_contacts()

            try:
                index = int(input("Enter contact number to delete: ")) - 1
                manager.delete_contact(index)

            except ValueError:
                print("Invalid input.")

        elif choice == '6':
            print("Exiting Contact Management System...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()