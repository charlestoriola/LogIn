import getpass
import os.path

# def create_file(filename):
# 	try:
# 		file = open(filename, "w")
# 	except:
# 		print("Error creating file")


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

	username_file = open('Database/usernames.bin', "a+")
	password_file = open('Database/password.bin', "a+")

	username_file.write(username+"\n")
	password_file.write(password+"\n")

	username_file.close()
	password_file.close()
