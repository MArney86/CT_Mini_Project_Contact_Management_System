import re

def add_contact(contact_list):
    name = get_contact_name()    
    phone = get_contact_phone()
    email = get_contact_email()

    choice = input("Do you have any additional info you'd like to add? (y/n)")
    while True:
        if choice == 'y':
            additional_info = get_contact_additional()
            break
        elif choice == 'n':
            additional_info = ""
            break
        else:
            print("That was not a y or n, please try again")
    
    if name.find(' ') == -1:
        unique_id = phone[-4:] + name
    else:
        name_space = name.find(' ')
        unique_id = phone[-4:] + name[:name_space]

    if unique_id not in contact_list.keys():
        contact_list[phone] = {'name': name, 'phone': phone, 'email': email, 'additional': additional_info}
    else:
        print("There's already a contact with that unique identifier")
    
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
    if re.match(validation, email):
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
                            print("Invalid email address: email adresses must have a valid top level domain") #return that the top level domain is invalid
                            return False
                        else:
                            print("Invalid email address: unknown email error")
                            return False
                    else: #invalid domain label
                        print("Invalid email address: email addresses must have a domain with a label of no more than 63 alphanumeric characters containing only alphanumeric character and . or -") #return the minimum requirements for email domain
                        return False
                else: #invalid identifier
                    print("Invalid email address: email addresses must have an identifier that contains alphanumeric characters and ._%+\-") #return the minimum requirements for the identifier part of the email address
                    return False
            else: #no @ symbol
                print("Invalid email address: email addresses must contain the @ symbol") #returns that the email address must contain an @ symbol
                return False
        except Exception:
            print("There was an error validating the email")

def validate_name(name):
    try:
        valid_name = r"[a-zA-Z]{2,}"
        valid_fullname = r"[a-zA-Z'-]{2,}+\s+[a-zA-Z'-]{2,}"
        if re.match(valid_name, name) or re.match(valid_fullname, name):
            return True
        else:
            return False
    except Exception:
        print("There was an unexpected error validating the name")


def validate_phone(phone):
    try:
        valid_phone = r'[0-9]{3}+-+[0-9]{3}+-+[0-9]{4}'
        if re.match(valid_phone, phone):
            return True
        else:
            return False
    except Exception:
        print("There was an error validating the phone number")

def get_contact_name():
    while True:
            name = input("What is the contact's name?: ").strip()
            valid_name = validate_name(name)
            if valid_name:
                break
            else:
                print("The name input did not meet minimum requirements. Please try again.")
    return name
        

def get_contact_phone():
    while True:
            phone = input("What is the contact's phone number (xxx-xxx-xxxx)?: ").strip()
            valid_phone = validate_phone(phone)
            if valid_phone:
                break
            else:
                print("The phone number input does not meet the format of ###-###-####. Please try again.")
    return phone

def get_contact_email():
    while True:
        email = input("What is the contact's email address?: ").strip()
        valid_email = validate_email(email)
        if valid_email:
            break
    return email

def get_contact_additional():
    try:
        additional = input("Please input any additional information for this contact: ").strip()
    except Exception:
        print("unexpected error while obtaining additional notes for contact")
    else:
        return additional

list_of_contacts = {}
# {'unique ID': {'name': '', 'phone': '', 'email': '', "additional": ''}, ...}

while True:
    print('''\nWelcome to the Contact Management System! 
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
