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
        print(unique_id)
    else:
        name_space = name.find(' ')
        unique_id = phone[-4:] + name[:name_space]
        print(unique_id)

    if unique_id not in contact_list.keys():
        contact_list[unique_id] = {'name': name, 'phone': phone, 'email': email, 'additional': additional_info}
        print(contact_list)
    else:
        print("There's already a contact with that unique identifier")
    
def edit_contact(contact_list):
    display_all(contact_list)
    user_choice = input("\nPlease input the unique id of the contact you wish to edit: ")
    uid_validation = r'[0-9]{4}+[a-zA-Z'-]{2,}'
    if re.match(uid_validation, user_choice):
        print('\nSelections for editing:\n1. Contact Name\n2. Contact Phone Number\n3. Contact Email Address\n4. Additional Information\n5. Return to Main Menu')
        choice = input("What would you like to edit?: ")
        while True:
            if choice == '1':
                while True:
                    new_name = input("What would you like to change the contact name to?")
                    if validate_name(new_name):
                        contact_list[user_choice]['name'] = new_phone
                        print(f"Name for contact {user_choice} is now :{contact_list[user_choice]['name']}")
                        break
                    else:
                        print("That was not a valid Name. Please try again")
                
            elif choice == '2':
                while True:
                    new_phone = input("What would you like to change the email address to?")
                    if validate_phone(new_phone):
                        contact_list[user_choice]['phone'] = new_phone
                        print(f"Phone Number for contact {user_choice} is now :{contact_list[user_choice]['phone']}")
                        break
                    else:
                        print("That was not a valid Phone Number. Please try again")
                
            elif choice == '3':
                while True:
                    new_email = input("What would you like to change the email address to?")
                    if validate_email(new_email):
                        contact_list[user_choice]['email'] = new_email
                        print(f"Email address for contact {user_choice} is now :{contact_list[user_choice]['email']}")
                        break
                    else:
                        print("Please try again")

            elif choice == '4':
                print(f"Current additional info for contact: \n{contact_list[user_choice]['additional']}")
                while True:
                    print('')
                    choice = input("Would you like to \n1. Add to current info\n2. Replace current info\n? :")
                    if choice == '1':
                        new_add = input("What would you like to add to the additional information: ")
                        contact_list[user_choice]['additional'] = contact_list[user_choice]['additional'] + ' ' + new_add
                        break
                    elif choice == '2':
                        contact_list[user_choice]['additional'] = input("What would you like to replace the current info with?\n: ")
                        break
                    else:
                        print("Not a valid selection: Please try again.")
                print(f"New additional info for contact {user_choice}:\n{contact_list[user_choice]['additional']}")        

            elif choice == '5':
                main(contact_list)
                break

            else:
                print("That was not a valid selection. Please try again.")


def locate_contact(contact_list, search_value):
    found = False
    found_contacts = []
    for unique_id, contact in contact_list.items():
        if search_value in contact.values():
            found_contacts.append(unique_id)
            found = True
        else:
            continue
    return (found, found_contacts)

def delete_contact(contact_list):
    display_all(contact_list)
    uid_validation = r'[0-9]{4}+[a-zA-Z'-]{2,}'
    while True:
        user_choice = input("\nPlease input the unique id of the contact you wish to edit: ").strip()
        try:
            if re.match(uid_validation, user_choice):
                contact_list.pop(user_choice)
                print("The contact with UniqueID '{user_choice}' was deleted")
                break
            else
                print("That UniqueID was not valid, please try again")
        except KeyError:
            print("Sorry there does not exist a contact with that UniqueID.")
        except Exception:
            print("An unknown Error Occurred")
        

def search_contacts(contact_list):
    while True:
        search_criteria = input("\nSearch criteria:\n1. By Name\n2. By Phone Number\n3. By email\n4.By Additional Information\n5.Return To Main Menu\nWhich criteria would you like to search by?: ")
        
        if search_criteria == '1':
            search_name = input("What name would you like to search for?: ")
            if validate_name(search_name):
                found, located_contacts = locate_contact(contact_list, search_name)
                if found:
                    print("Contacts found with that name:")
                    found_name = False
                    for uid in located_contacts:
                        if contact_list[uid]['name'] == search_name:
                            found_name = True
                            display_contact(contact_list, uid)
                        else:
                            continue
                    if not found_name:
                        print("There were no contacts with that name listed as contact name")
                else:
                    print("There were no contacts with that name found")
            else:
                print("That was not a valid name for searching")
            break

        if search_criteria == '2':
            search_phone = input("What phone number would you like to search for?: ")
            if validate_phone(search_phone):
                found, located_contacts = locate_contact(contact_list, search_phone)
                if found:
                    print("Contacts found with that phone number:")
                    found_phone = False
                    for uid in located_contacts:
                        if contact_list[uid]['phone'] == search_phone:
                            found_phone = True
                            display_contact(contact_list, uid)
                        else:
                            continue
                    if not found_phone:
                        print("There were no contacts with that phone number listed as contact phone number")
                else:
                    print("There were no contacts with that phone number found")
            else:
                print("That was not a valid phone number for searching")
            break

        if search_criteria == '3':
            search_email = input("What email address would you like to search for?: ")
            if validate_name(search_email):
                found, located_contacts = locate_contact(contact_list, search_email)
                if found:
                    print("Contacts found with that email address:")
                    found_email = False
                    for uid in located_contacts:
                        if contact_list[uid]['name'] == search_email:
                            found_email = True
                            display_contact(contact_list, uid)
                        else:
                            continue
                    if not found_name:
                        print("There were no contacts with that email address listed as contact email address")
                else:
                    print("There were no contacts with that email address found")
            else:
                print("That was not a valid email address for searching")
            break

        if search_criteria == '4':
            search_additional = input("Please input the string you'd like to search for in the additional info of the contact you're looking for:\n ")
            search_rgx = rf'\b{re.escape(search_additional)}'
            for uid, content in contact_list.items
                found_add = False
                if re.match(search_rgx, contact_list[uid]['additional'], re.IGNORECASE):
                    found_add = True
                    display_contact(contact_list, uid)
                else:
                    continue
            if not found:
                print(f'There were no contacts with "{search_additional}" in their Additional Information')
            break

        if search_criteria == '5':
            main(contact_list)
            break
            


def display_contact(contact_list, unique_id)
    print(unique_id + ": \n\tName: " + contact_list[unique_id]["name"] + "\n\tPhone Number: " + contact_list[unique_id]["phone"] + "\n\tEmail Address: " + contact_list[unique_id]["email"] + "\n\tAdditional Notes: " + contact_list[unique_id]["additional"])


def display_all(contact_list):
    for unique_id, contact in contact_list.items():
        output = unique_id + ": \n\tName: " + contact["name"] + "\n\tPhone Number: " + contact["phone"] + "\n\tEmail Address: " + contact["email"] + "\n\tAdditional Notes: " + contact["additional"]
        print(output)

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
        valid_name = r"[a-zA-Z'-]{2,}"
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

def main(list_of_contacts):
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

list_of_contacts = {}
# {'unique ID': {'name': '', 'phone': '', 'email': '', 'additional': ''}, ...}

main(list_of_contacts)