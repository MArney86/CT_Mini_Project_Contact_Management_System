Contact Management System Mini Project for Coding Temple Software Engineering Course
This application is a Contact Management System for adding, modifying, and storing your contacts written in Python3 with no external dependencies.

Table of Contents:
	1. Installing and Running the Application
	2. How to use the Contact Management System
		a. The Main Menu
		b. Adding a new contact
		c. Edit an existing contact
		d. Delete a contact
		e. Search for a contact
		f. Display all contacts
		g. Export contacts to a text file
		h. Import contacts from a text file
		i. Quit the program

1. Installing and Running the Application:
	Installation: Clone or download the repository to a directory.

	Running the Application on Windows:
		python .\Contact_Management_System.py (if Python is setup in your system's PATH)
		[installation Directory]\python.exe .\Contact_Management_System.py (no system PATH set)

	Running the Application on POSIX Operating Systems(Linux/Unix/BSD/MacOS):
		python ./Contact_Management_System.py (if proper environment variables setup)
		python3 ./Contact_Management_System.py (some systems may require python3 command instead of python command)
		[install path]/python ./Contact_Management_System.py (no environment variable set)
		[install path]/python3 ./Contact_Management_System.py (alternative for some systems with no environment variable set)

2. How to use the Contact Management System:
	a.The Main Menu
		Welcome to the Contact Management System! 
		Menu:
		1. Add a new contact
		2. Edit an existing contact
		3. Delete a contact
		4. Search for a contact
		5. Display all contacts
		6. Export contacts to a text file
		7. Import contacts from a text file
		8. Quit
		Here the user choses what they would like to do with their contacts, be it add a new one, editing one, finding a contact, or storing/loading existing contacts from a file
		
	b. Adding a new contact:
		Here the user is prompted for information to add a new contact and generating a unique id for that contact from the contact data. The user will be asked if they want to add additional information for their contact or not; if not, the additional information will be set to empty.
			Names must contain atleast 2 characters (per name if first and last are input) and are limited to alphabet characters and the ' and - characters
			Phone numbers must be in format ###-###-#### with only numbers accepted
			Email addresses must alphanumeric characters plus ._%+- and no longer than 64 characters for the identifies, an @ symbol, alphanumeric characters and .- not at beginning or end of domain name and no longer than 63characters, and finally a top level domain of atleast 2 alphabet characters.
	
	c. Edit an existing contact:
		Here the user will edit a contact already in their collection of contacts
		The list of contacts will be printed and the user will be asked which contact they would like to edit by choosing the contact by it's unique identifier.
		Once the contact has been chosen the following menu will come up:
			Selections for editing:
			1. Contact Name
			2. Contact Phone Number
			3. Contact Email Address
			4. Additional Information
			5. Return to Main Menu
			
			1 - Contact Name:
				Asks the user what valid name they want to change the contact's name to and changes it.
			2 - Contact Phone Number
				Asks the user what valid phone number they want to change the contact's phone number to and changes it.
			3 - Contact Email Address
				Asks the user what valid email address they want to change the contact's email address to and changes it.
			4 - Additional Information
				Asks the user if they want to add to the additional information or overwrite it all together.
				Addition will just add the new information after a space and overwriting will completely replace the already existing information
			5 - Return to Main Menu
				Returns the program to the Main Menu

	d. Delete a contact:
		Displays the list of all contacts to allow the user to easier choose the unique identifier of the contact they would like to delete.
		Then the user is asked for the unique identifier of the contact that they would like to delete and then deletes the contact.

	e. Search for a contact:
		Here the user searches for a specific contact using the various information in the contacts 
		The program will load this menu for the user to select the information they would like to use to search for the sought contact:		
			Search criteria:
			1. By Name
			2. By Phone Number
			3. By email
			4. By Additional Information
			5.Return To Main Menu
 
			1 - Asks the user for the valid name they would like to search for then displays any matching contacts or a message letting the user know there are none.

			2 - Asks the user for the valid phone number they would like to search for then displays any matching contacts or a message letting the user know that there are none.

			3 - Asks the user for the valid email address they would like to search for then displays any matching contacts or a message letting the user know that there are none.

			4 - Asks the user for a string they would like to search the additional information of the contacts for and then displays any matching contacts or a message letting the user know that there are none.

			5 - Returns the program to the Main Menu

	f. Display all contacts:
		This selection displays all the contacts the user had recorded at the time of selection

	g. Export contacts to a text file:
		This option asks the user for a filename (will load/create file from the directory of the program itself) or filepath (will load/create file from the filepath given) to a file to save the contacts information to, will create file if it does not previously exist.
		test_contacts.txt is provided to test the functionality and show basic format.

	h. Import contacts from a text file:
		This option asks the user for a filename (will load file from the directory of the program itself) or filepath (will load file from the filepath given) then will load contacts saved in the same format this program saves in to the program.
		test_contacts.txt is provided to test the functionality and show basic format.

	i. Quit:
		This option will exit the program back to the system/terminal prompt.