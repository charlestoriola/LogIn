import getpass
import os.path
from os import system

def next():
    if not input("Press ENTER to continue"):
        system("clear")
        return
    else:
        system("clear")
        next()


def whitespace_remove(word):
	whitespace = word.count(' ')
	if(' ' in word):
		for whitespace in word:
			word = "".join(word.split())
	return word


def whitespace_found(username):
	choice = ''

	while (choice != 'y' or choice != 'Y'):
		newusername = whitespace_remove(username)
		
		print("\nYou left some spaces there")
		choice = input("Would you like to enter your username again?(Y/N) ")
		print("\n")
		if choice == 'n' or choice == 'N':
			print("Whitespaces removed\n")
			username = newusername
			print("\n Your username is ", username)
			break
		elif choice == 'y' or choice == 'Y':
			username = input("Enter username: ")
			if (' ' in username):
				username = whitespace_found(username)
			return username



def sign_up(username, password):
	
	if (' ' in username):
		username = whitespace_found(username)


	username_file = open('Database/usernames.bin', "a+")
	password_file = open('Database/password.bin', "a+")

	username_file.write(username+"\n")
	password_file.write(password+"\n")

	username_file.close()
	password_file.close()

	return username


def log_in(username, password):

	username_file = open('Database/usernames.bin', "r")
	password_file = open('Database/password.bin', "r")

	userfound = False
	pwfound = False

	for i in username_file:
		if i[:-1] == username:
			userfound = True
			

	for i in password_file:
		if i[:-1] == password:
			pwfound = True
			

	if userfound and pwfound:
		password_file.close()
		username_file.close()
		return True
	else:
		username_file.close()
		password_file.close()
		return False