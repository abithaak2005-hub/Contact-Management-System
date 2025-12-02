
contacts = {}

def create_contact():
    cid = input("Enter Contact ID: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[cid] = {"name": name, "phone": phone}
    print("Contact added successfully!\n")

def view_all_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    print("---- All Contacts ----")
    for cid, info in contacts.items():
        print(f"ID: {cid}, Name: {info['name']}, Phone: {info['phone']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for cid, info in contacts.items():
        if info["name"].lower() == name.lower():
            print(f"Found! ID: {cid}, Name: {info['name']}, Phone: {info['phone']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_phone():
    cid = input("Enter Contact ID to update: ")
    if cid in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[cid]["phone"] = new_phone
        print("Phone updated successfully!\n")
    else:
        print("Contact ID not found.\n")

def delete_contact():
    cid = input("Enter Contact ID to delete: ")
    if cid in contacts:
        del contacts[cid]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

while True:
    print("1. Create New Contact")
    print("2. View All Contacts")
    print("3. Search Contact by Name")
    print("4. Update Phone Number")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        view_all_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_phone()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.\n")