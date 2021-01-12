import getpass

def fileExists(filename):
	try:
    	f = open(filename)
	except IOError:
    	
	finally:
    	f.close()

def whitespaceRemove(word):
	whitespace = word.count(' ')
	if(' ' in word):
		for whitespace in word:
			word = "".join(word.split())
	return word

def signUp():
	choice = ''

	username = ""
	while (choice != 'y' or choice != 'Y'):
		print("Whitespaces are not allowed")
		username = input("Enter username: ")


		if (' ' in username):
			newusername = whitespaceRemove(username)
			
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
	print(password)

	username_file = open('usernames.bin', "r")