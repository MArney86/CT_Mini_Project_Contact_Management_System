import re
import sys

def add_contact(contact_list): #function for adding a new contact
    name = get_contact_name() #get the contact's name from the user
    phone = get_contact_phone() #get the contact's phone number from the user
    email = get_contact_email() #get the contact's email from the user

    choice = input("Do you have any additional info you'd like to add? (y/n)") #ask the user if they want to add any additional info for the contact
    while True: #loop incase of incorrect inputs
        if choice == 'y': #user chooses yes
            additional_info = get_contact_additional() #get additional information from the user
            break # end the loop
        elif choice == 'n': #user chooses no
            additional_info = "" #input an empty string in the additional information
            break # end the loop
        else: #improper input
            print("That was not a y or n, please try again") #notify user of improper input
    
    if name.find(' ') == -1: #there isnot  a space in the name in case that it's a full name
        unique_id = phone[-4:] + name #make the unique id from the last 4 of the phone number and the name
    else: #there is a space
        name_space = name.find(' ') #find the index of the space
        unique_id = phone[-4:] + name[:name_space] #make the unique id from the last 4 of the phone number and the first name

    if unique_id not in contact_list.keys(): #check for the unique id to not be in a list of the keys in the contact_list dictionary
        contact_list[unique_id] = {'name': name, 'phone': phone, 'email': email, 'additional': additional_info} #add the contact to the contact list dictionary
    else: #unique id is in the list of contact keys
        print("There's already a contact with that unique identifier") #notify the user of contact with that unique id already existing
    
def edit_contact(contact_list): #function for editing contacts
    display_all(contact_list) #display all the contacts to help user choose
    user_choice = input("\nPlease input the unique id of the contact you wish to edit: ") #get the unique id of the contact the user wants to change
    uid_validation = r"[0-9]{4}+[a-zA-Z'-]{2,}" #regex to validate the input as a valid unique id
    if re.match(uid_validation, user_choice): #check that the unique id is valid
        while True: #loop incase of invalid inputs
            print('\nSelections for editing:\n1. Contact Name\n2. Contact Phone Number\n3. Contact Email Address\n4. Additional Information\n5. Return to Main Menu') #display sub-menu
            choice = input("What would you like to edit?: ") #get menu choice from user
            if choice == '1': #user chose to change name
                while True: #loop incase of invalid inputs
                    new_name = input("What would you like to change the contact name to?") #ask user for new name
                    if validate_name(new_name): #check if input is valid
                        contact_list[user_choice]['name'] = new_name #change the name to the user's input
                        print(f"Name for contact {user_choice} is now :{contact_list[user_choice]['name']}") #notify user of change
                        break #end loop
                    else: #invalid name
                        print("That was not a valid Name. Please try again") #notification of invalid input

            elif choice == '2': #user chose to edit
                while True: #loop incase of invalid inputs
                    new_phone = input("What would you like to change the phone number to?") #ask user for new phone number
                    if validate_phone(new_phone): #check if input is valid
                        contact_list[user_choice]['phone'] = new_phone #change phone number to user input
                        print(f"Phone Number for contact {user_choice} is now :{contact_list[user_choice]['phone']}") #notify user of change
                        break #end loop
                    else: #invalid phone number
                        print("That was not a valid Phone Number. Please try again") #notification of invalid input
                
            elif choice == '3':
                while True: #loop incase of invalid inputs
                    new_email = input("What would you like to change the email address to?") #ask for new email address
                    if validate_email(new_email): #check if input is valid
                        contact_list[user_choice]['email'] = new_email
                        print(f"Email address for contact {user_choice} is now :{contact_list[user_choice]['email']}") #notify user of change
                        break #end loop
                    else: #invalid email address
                        print("Please try again") #notification of invalid input

            elif choice == '4':
                print(f"Current additional info for contact: \n{contact_list[user_choice]['additional']}")
                while True: #loop incase of invalid inputs
                    choice = input("Would you like to \n1. Add to current info\n2. Replace current info\n? :") #ask user how they want to change the current additional information
                    if choice == '1': #user choose to add to the additional information
                        new_add = input("What would you like to add to the additional information: ") #get new information from the user
                        contact_list[user_choice]['additional'] = contact_list[user_choice]['additional'] + ' ' + new_add #add new input to end of additional info
                        break #end loop
                    elif choice == '2': #user chooses to overwrite the additional input
                        contact_list[user_choice]['additional'] = input("What would you like to replace the current info with?\n: ") #store the user's new information in the additional information
                        break #end loop
                    else: #invalid choice
                        print("Not a valid selection: Please try again.") #notify user of invalid choice
                print(f"New additional info for contact {user_choice}:\n{contact_list[user_choice]['additional']}") #notify user of change

            elif choice == '5': #user chooses to return to main menu
                break #end the loop and return to previous function

            else: #invalid choice
                print("That was not a valid selection. Please try again.") #notify user of invalid choice

def locate_contact(contact_list, search_value): #function to find contacts with given input in their values
    found = False #found flag
    found_contacts = [] #empty list of found contacts
    for unique_id, contact in contact_list.items(): #loop through contacts
        if search_value in contact.values(): #check if the input is in any of the values in the contact inner dictionary
            found_contacts.append(unique_id) #store found contact unique identifier in found contacts list
            found = True #set found flag true
        else: #not in contacts inner values
            continue #next iteration
    return (found, found_contacts) #return tuple of found flag and list of found contacts

def delete_contact(contact_list): #function to delete a contact
    if contact_list: #check that contact list is not empty
        display_all(contact_list) #display all contacts
        uid_validation = r"[0-9]{4}+[a-zA-Z'-]{2,}" #validation regex for unique identifiers
        while True: #loop in case of improper choice
            user_choice = input("\nPlease input the unique id of the contact you wish to delete: ") #get the unique identifier of the contact the user want's to delete
            try: #try block for error handling
                if re.match(uid_validation, user_choice): #check that user input is valid
                    contact_list.pop(user_choice) #remove the contact with unique identifier recieved from the user
                    print(f"The contact with UniqueID '{user_choice}' was deleted") #notify user of deletion
                    break #end the loop
                else: #input was invalid
                    print("That UniqueID was not valid, please try again") #notify user of invalid input
            except KeyError: #there is a key error
                print("Sorry there is not a contact with that UniqueID.") #notify user that the key isn't in the contact list dictionary
            except Exception: #general exception
                print("An unknown Error Occurred") #notify user of error
    else: # contact list is empty
        print("There aren't any contacts to delete at this moment") #notify user of empty contact list

def search_contacts(contact_list): #function to search contacts
    while True: #loop in case of improper input
        search_criteria = input("\nSearch criteria:\n1. By Name\n2. By Phone Number\n3. By email\n4. By Additional Information\n5.Return To Main Menu\nWhich criteria would you like to search by?: ") #search method menu
         
        if search_criteria == '1':  #user choses to search by name
            search_name = input("What name would you like to search for?: ") #get the name the user is searching for
            if validate_name(search_name): #check if the name from the user is valid
                found, located_contacts = locate_contact(contact_list, search_name) #run the user input through the function that locates contacts that have that name in them and store the return in 2 variables
                if found: #check found flag for found contacts
                    print("Contacts found with that name:") #print heading for found contacts
                    found_name = False #flag for checking found contacts have the name under the name key
                    for uid in located_contacts: #iterate through the found contacts list
                        if contact_list[uid]['name'] == search_name: #check if the iterated contact has the input under the name key
                            found_name = True #change key for found contacts with the name under the name key
                            display_contact(contact_list, uid) #display contact that matches
                        else: #iterated contact doesn't have the input under the name key
                            continue #go on to next iteration
                    if not found_name: #no contacts had the input under the proper name key
                        print("There were no contacts with that name listed as contact name") #notify user of lack of matches
                else:# no found contacts
                    print("There were no contacts with that name found") #notify user of lack of matches
            else: #name is invalid
                print("That was not a valid name for searching") #notify user that input is invalid
            break #end loop

        if search_criteria == '2': #user chooses to search by phone number
            search_phone = input("What phone number would you like to search for?: ") #get phone number to search for from user
            if validate_phone(search_phone): #test that the phone number input is valid
                found, located_contacts = locate_contact(contact_list, search_phone) #find contacts that have the input phone number in them
                if found: #check if found flag is true
                    print("Contacts found with that phone number:") #heading for found contacts
                    found_phone = False #set flag for found contacts with phone number under the phone key
                    for uid in located_contacts: #iterate through found contacts
                        if contact_list[uid]['phone'] == search_phone: #check contact from list has the input under the phone key
                            found_phone = True #set found under phone key flag to true
                            display_contact(contact_list, uid) #display contact with input under the phone key
                        else: #input is not under the phone key
                            continue #on to next iteration
                    if not found_phone: #no contacts found with input under phone key
                        print("There were no contacts with that phone number listed as contact phone number") #notify user of lack of matches
                else: #found flag was false
                    print("There were no contacts with that phone number found") #notify user of lack of matches
            else: #invalid phone number
                print("That was not a valid phone number for searching") #notify user of invalid phone number
            break #end loop

        if search_criteria == '3': #user chooses to search by email
            search_email = input("What email address would you like to search for?: ") #get the email address to search with from user
            if validate_email(search_email): #check that the input is valid
                found, located_contacts = locate_contact(contact_list, search_email) #get found flag and list of contacts with email address in them
                if found: #found flag is true
                    print("Contacts found with that email address:") #heading for found contacts
                    found_email = False #flag for found contacts with input under email key
                    for uid in located_contacts: #iterate through found contacts
                        if contact_list[uid]['email'] == search_email: #check that contact has the email address under the email key
                            found_email = True #change found flag to true
                            display_contact(contact_list, uid) #display contact with input under the email key
                        else: #input not under email key
                            continue #on to next contact
                    if not found_email: #no contacts with input under email key
                        print("There were no contacts with that email address listed as contact email address") #notify user of lack of matches
                else: #no found contacts
                    print("There were no contacts with that email address found") #notify user of lack of matches
            else: #invalid input
                print("That was not a valid email address for searching") #notify user of invalid input
            break #end the loop

        if search_criteria == '4': #user chooses to search the addition notes
            search_additional = input("Please input the string you'd like to search for in the additional info of the contact you're looking for:\n ") #get sub string to search for from user
            found_add = False #found flag initialized to false
            found_list = [] #empty found list
            for uid, content in contact_list.items(): #iterate through the key:value pairs in the contact_list
                if content['additional'].find(search_additional) > -1: #check that the substring is found in the additional info of the currently iterated contact
                    found_add = True #change found flag to true
                    found_list.append(uid) #add unique identifier of found contact to found list
                else: #substring not in additional info of contact
                    continue #on to next iteration
            if found_add: #check that contacts are found
                print(f'Contacts with "{search_additional}" in their additional information:') #heading for found contacts
                for unique in found_list: #iterate through found list
                    display_contact(contact_list, unique) #display current found contact
            else: #no contacts found
                print(f'There were no contacts with "{search_additional}" in their Additional Information') #notify user of lack of matches
            break #end loop

        if search_criteria == '5': #user wants to return to Main Menu
            break #end loop and return to previous function

        else: #invalid input
            print("That selection was invalid. Please try again") #notify user of invalid input

def display_contact(contact_list, unique_id): #function to display a single contact
    print(f"{unique_id.strip()}:\n\tName: {contact_list[unique_id]["name"]}\n\tPhone Number: {contact_list[unique_id]["phone"]}\n\tEmail Address: {contact_list[unique_id]["email"]}\n\tAdditional Notes: {contact_list[unique_id]["additional"]}") #format and display info from the contact with the unique identifier given

def display_all(contact_list): #function to display all contacts
    for unique_id, contact in contact_list.items(): #iterate through the contact list
        output = f"{unique_id.strip()}:\n\tName: {contact["name"]}\n\tPhone Number: {contact["phone"]}\n\tEmail Address: {contact["email"]}\n\tAdditional Notes: {contact["additional"]}" #format info from iterated contact for output
        print(output) #print formatted contact output

def export_contacts(contact_list): #function to export contacts to text file
    file_name = input("\nWhat is the name of the file you wish to save your contacts in?: ") #get the filename of filepath of the output file from user 
    try: #try block for error handling
        with open(file_name, 'w') as output_file: #open file from user
            for uid, content in contact_list.items(): #iterate throught the contacts
                output_file.write(f"UID:{uid}") #write a line with the unique identifier of the contact to file
                for key, value in content.items(): #iterate through the key:value pairs of the contact dictionary
                    output_file.write(f"{key}:{value}\n") #write a line with the key:value pair of the contact dictionary to file
                output_file.write('\n') #write empty line to seperate contacts for human readability
    except PermissionError: #a permission error occurs
        print("PermissionError: There seems to be some permission issues.") #notify user of error
    except Exception: #general exceptions
        print("There was an unexpected error") #notify user of error

def import_contacts(contact_list): #function to import contacts from a text file
    file_name = input("\nWhat is the name of the file you wish to load contacts from?: ") #get filename or filepath of input file from user
    try: #try block for error handling
        with open(file_name, 'r') as input_file: #open file from user
            counter = 0 #counter to keep track of line position in file's contents
            lines = input_file.readlines() #save list of lines from the file
            for counter in range(len(lines)): #iterate through the list of lines from file
                line = lines[counter] #copy line at current counter value
                if not line.isspace(): #check that line has content
                    line = line[:-1] #remove trailing new lines from input
                    key, value = line.split(":") #split the line at the colon character and store in variables key and value
                    if key == 'UID':  #check that key value is 'UID'
                        contact_internal = {} #temporary storage for contact entry
                        for x in range(1,5): #iterate through next 4 lines
                            contact_key, contact_value = lines[counter+x].split(':') #split line at colon
                            contact_internal[contact_key] = contact_value[:-1] #add the key:value pair to temporary contact storage removing trailing newlines
                        counter += 4 #update the counter now that we've just iterated over 4 lines
                        if value not in contact_list.keys(): #check that read unique identifier isn't already in the contact list
                            contact_list[value] = contact_internal #add contact to contact list with the unique identifier read from file
                            print(f'Contact "{value}" has been added') #notify user of addition of contact
                        else: #unique identifier already exist
                            print(f'Contact {value} already exists in your contacts, skipping.') #notify user that unique identifier already exists
                    counter += 1 #update counter for initial iteration
    except FileNotFoundError: #file not found error occurs
        print("That file does not exist.") #notify user of file not found
    except Exception: #general exceptions
        print("There was an unexpected error") #notify user of error
        
def validate_email(email): #validate email data
    validation = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$' #regex to validate email given
    if re.match(validation, email): #check that given email matches the validation regex
        return True #return true value
    else: #email does not meet validation requirements
        try: #try block for error handling
            if '@' in email: # verify that the
                split_email = email.split("@") #split the email at the @ symbol for easier testing
                valid_id = r'^[A-Za-z0-9._%+-]' #validation regex for email identifier
                if split_email[0] and len(split_email[0]) <= 64 and re.match(valid_id,split_email[0]): #check for valid identifier in the email address
                    split_domain = split_email[1].split(".") #split the domain by the '.' symbol for validity
                    valid_domain = r'[A-Za-z0-9.-]' #validation regex for domain identifier
                    if len(split_domain[0]) <= 63 and re.match(valid_domain, split_domain[0]): #check for valid domain name
                        valid_top_domain = '[A-Z|a-z]{2,}$' #validation regex for top level domain
                        if not re.match(valid_top_domain,split_domain[1]): #check that the top level domain is not valid
                            print("Invalid email address: email adresses must have a valid top level domain") #return that the top level domain is invalid
                            return False #return false value
                        else:
                            print("Invalid email address: unknown email error") #notify user of unknown validation error
                            return False #return false value
                    else: #invalid domain label
                        print("Invalid email address: email addresses must have a domain with a label of no more than 63 alphanumeric characters containing only alphanumeric character and . or -") #return the minimum requirements for email domain
                        return False #return false value
                else: #invalid identifier
                    print("Invalid email address: email addresses must have an identifier that contains alphanumeric characters and ._%+\-") #return the minimum requirements for the identifier part of the email address
                    return False #return false value
            else: #no @ symbol
                print("Invalid email address: email addresses must contain the @ symbol") #returns that the email address must contain an @ symbol
                return False #return false value
        except Exception: #general exception
            print("There was an error validating the email") #notify user of error

def validate_name(name): #function to validate name data
    try: #try block for error handling
        valid_name = r"[a-zA-Z'-]{2,}" #validation regex for single name
        valid_fullname = r"[a-zA-Z'-]{2,}+\s+[a-zA-Z'-]{2,}" #validation regex for full name
        if re.match(valid_name, name) or re.match(valid_fullname, name): #check that given name is valid
            return True #return true value
        else: #name does not validate
            return False #return false value
    except Exception: #general exceptions
        print("There was an unexpected error validating the name") #notify user of error

def validate_phone(phone): #function to verify phone number data
    try: #try block for error handling
        valid_phone = r'[0-9]{3}+-+[0-9]{3}+-+[0-9]{4}' #regex to verify phone number given
        if re.match(valid_phone, phone): #verify that phone number matches the validation regex
            return True #return true value
        else: #phone number does not validate
            return False #return false value
    except Exception: #general exception
        print("There was an error validating the phone number") #notify user of error

def get_contact_name(): #get contact name from user
    while True: #loop in case of invalid input
            name = input("What is the contact's name?: ").strip() #get name from user
            if validate_name(name): #check if name input is valid 
                break #end loop
            else: #name does not validate
                print("The name input did not meet minimum requirements. Please try again.") #notify user of invalid input
    return name #retun validated name

def get_contact_phone(): #get contact phone number from user
    while True: #loop in case of invalid input
            phone = input("What is the contact's phone number (xxx-xxx-xxxx)?: ").strip() #get phone number for contact from user
            if validate_phone(phone): #check that input phone number is valid
                break #end loop
            else: #input does not validate
                print("The phone number input does not meet the format of ###-###-####. Please try again.") #notify user of invalid input
    return phone #return valid input

def get_contact_email(): #get email input for contact from user
    while True: #loop in case of invalid input
        email = input("What is the contact's email address?: ").strip() #get email input from user
        if validate_email(email): #check if email input is valid
            break #end loop
        #no else because errors in email formatting will be printed by validation function      
    return email  #return valid input

def get_contact_additional(): #get additional information from user
    try: #try block for error handling
        additional = input("Please input any additional information for this contact: ").strip() #get additional information from user
    except Exception: #general exception
        print("unexpected error while obtaining additional notes for contact") #notify user of error
    else: #no errors occured
        return additional #return the additional information given

def main(list_of_contacts): #main menu function/main loop of the program
    while True: #loop in case of invalid input
        print('''\nWelcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit''') #print the main menu
        choice = input("What would you like to do with your contacts?: ")

        if choice == '1': #chose add contact
            add_contact(list_of_contacts) #run function for new contact
        elif choice == '2': #chose edit contact
            edit_contact(list_of_contacts) #run function to edit contact
        elif choice == '3': #chose delete contact
            delete_contact(list_of_contacts) #run function to delete contact
        elif choice == '4': #chose search contact
            search_contacts(list_of_contacts) #run function to search contacts
        elif choice == '5': #chose display all contacts
            display_all(list_of_contacts) #run function to display all contacts
        elif choice == '6': #chose to export contacts to txt file
            export_contacts(list_of_contacts) #run function to export contact list to text file
        elif choice == '7': #chose to import contacts from txt file
            import_contacts(list_of_contacts) #run function to import contacts from text file
        elif choice == '8': #chose to exit
            sys.exit("Goodbye!!!") #exit program to system/terminal prompt
        else: #invalid choice
            print("That was not a valid choice. Please try again.") #notify user of invalid choice

list_of_contacts = {} #empty dictionary to start the program with
# {'unique ID': {'name': '', 'phone': '', 'email': '', 'additional': ''}, ...}

main(list_of_contacts) #start the program by calling the main menu function