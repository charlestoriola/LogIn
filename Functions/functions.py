import getpass

def whitespace_remove(word):
	whitespace = word.count(' ')
	if(' ' in word):
		for whitespace in word:
			word = "".join(word.split())
	return word

def sign_up():
	choice = ''

	username = ""
	while (choice != 'y' or choice != 'Y'):
		print("Whitespaces are not allowed")
		username = input("Enter username: ")


		if (' ' in username):
			newusername = whitespace_remove(username)
			
			print("\nYou left some spaces there")
			choice = input("Would you like to enter your username again?(Y/N) ")
			print("\n")
			if choice == 'n':
				print("Whitespaces removed\n")
				break
		else:
			choice = ''
			break

	password = getpass.getpass()

	username_file = open('usernames.bin', "w")
	password_file = open('password.bin', "w")

	username_file.write(username)
	password_file.write(password)
