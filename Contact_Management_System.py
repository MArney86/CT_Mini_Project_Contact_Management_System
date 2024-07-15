def add_contact(contact_list):
    pass

def edit_contact(contact_list):
    pass

def delete_contact(contact_list):
    pass

def search_contacts(contact_list):
    pass

def display_all(contact_list):
    pass

def export_contacts(contact_list):
    pass

def import_contacts(contact_list):
    pass

list_of_contacts = {}
# {'unique ID': {'name': '', 'phone': '', 'email': '', "additional": ''}, ...}

while True:
    print('''Welcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit''')
    choice = input("What would you like to do with your contacts?: ")

    if choice == '1':
    elif choice == '2':
    elif choice == '3':
    elif choice == '4':
    elif choice == '5':
    elif choice == '6':
    elif choice == '7':
    elif choice == '8':
        break
    else:
        print("That was not a valid choice. Please try again.")
