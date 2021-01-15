from Functions.functions import *

print("Welcome User")
next()

flag = False
while flag == False:

	menu = int(input("1.Sign Up\n2.Log In\n0.Exit\n"))
	if menu == 1:
		print("Whitespaces are not allowed")
		username = input("Enter username: ")
		password = getpass.getpass()

		username = sign_up(username, password)

		flag = True
	elif menu == 2:
		username = input("Enter username: ")
		password = getpass.getpass()

		success = log_in(username, password)

		if success:
			print("Success\n")
			flag = True
		else:
			print("Try Again\n")			

	elif menu == 0:
		exit()
		
	else:
		print("Invalid Choice\n")


system("clear")
print("Welcome ", username)
next()
print("What's good?")