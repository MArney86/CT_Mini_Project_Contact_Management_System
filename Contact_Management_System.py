import re

def add_contact(contact_list):
    name = get_contact_name()    
    phone = get_contact_phone()
    email = get_contact_email()

    choice = input("Do you have any additional info you'd like to add? (y/n)")
    while True:
        if choice == 'y':
            additional_info = get_contact_additional()
        elif choice == 'n':
            break
        else:
            print("That was not a y or n, please try again")
    

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

def validate_email(email):
    validation = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    if re.match(validation, email)
        return True
    else:
        try:
            if '@' in user_email: # verify that the
                split_email = user_email.split("@") #split the email at the @ symbol for easier testing
                valid_id = r'^[A-Za-z0-9._%+-]'
                if split_email[0] and len(split_email[0]) <= 64 and re.match(valid_id,split_email[0]): #check for valid identifier in the email address
                    split_domain = split_email[1].split(".") #split the domain by the '.' symbol for validity
                    valid_domain = r'[A-Za-z0-9.-]'
                    if len(split_domain[0]) <= 63 and re.match(valid_domain, split_domain[0]): #check for valid domain name
                        valid_top_domain = '[A-Z|a-z]{2,}$'
                        if not re.match(valid_top_domain,split_domain[1]): #check that the top level domain is not valid
                            return "Invalid email address: email adresses must have a valid top level domain" #return that the top level domain is invalid
                        else:
                            return"Invalid email address: unknown email error" 
                    else: #invalid domain label
                        return "Invalid email address: email addresses must have a domain with a label of no more than 63 alphanumeric characters containing only alphanumeric character and . or -" #return the minimum requirements for email domain
                else: #invalid identifier
                    return "Invalid email address: email addresses must have an identifier that contains alphanumeric characters and ._%+\-" #return the minimum requirements for the identifier part of the email address
            else: #no @ symbol
                return "Invalid email address: email addresses must contain the @ symbol" #returns that the email address must contain an @ symbol
        except Exception:
            print("There was an error validating the email")

def validate_name(name):
    pass

def validate_phone(phone):
    pass

def get_contact_name():
    while True:
        try:
            name = input("What is the contact's name?: ")
            valid_name = validate_name(name)
            if valid_name is bool:
                if valid_name:
                    break
                else:
                    raise ValueError
            else:
                if valid_name is str:
                    print(valid_name)
                else:
                    raise ValueError
    
        except ValueError:
            print("The input caused an unexpected error, please try again")
    
    return name
        

def get_contact_phone():
    while True:
        try:
            phone = input("What is the contact's phone number?: ")
            valid_phone = validate_phone(phone)
            if valid_phone is bool:
                if valid_phone:
                    break
                else:
                    raise ValueError
            else:
                if valid_phone is str:
                    print(valid_phone)
                else:
                    raise ValueError
        except ValueError:
            print("The input caused an unexpected error, please try again")
    
    return phone

def get_contact_email():
    pass

def get_contact_additional():
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
        add_contact(list_of_contacts)
    elif choice == '2':
        edit_contact(list_of_contacts)
    elif choice == '3':
        delete_contact(list_of_contacts)
    elif choice == '4':
        search_contacts(list_of_contacts)
    elif choice == '5':
        display_all(list_of_contacts)
    elif choice == '6':
        export_contacts(list_of_contacts)
    elif choice == '7':
        import_contacts(list_of_contacts)
    elif choice == '8':
        break
    else:
        print("That was not a valid choice. Please try again.")
