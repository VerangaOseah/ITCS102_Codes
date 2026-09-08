#getpass
import getpass 

username = "oseah"
password = "123456"

u = input("Enter Username: ")
p = getpass.getpass("Enter Password: ")

if username == u and password == p:
	print("Access Granted")
else: 
	print("Access Denied")
