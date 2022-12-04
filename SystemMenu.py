import time
import sys

for welcome in range(0,1):
    print("Hello User, I am Adrayle Perez Ebon 1st year BSIT Student\n")
    break

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("MENU:")

menu=input("""
1. Log in
2.Add student
3.Remove student
4.exit\n""")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

userInfo = ["admin","admin1","admin2"]
passInfo = ["password","password1","passwor2"]

print("Let's Start!")
option=int(input("Please Choose: "))
print("Please wait...\n")
    
if option == 2:
    time.sleep(2)
    print("processing...\n")
    time.sleep(2)
    
    name=input("Enter Student Name: ")
    age=int(input("Enter Age: "))
    bday=input("Birthday: ")
    time.sleep(2)
    print("Successful!!!\n")
    exit()
    
if option == 3:
    time.sleep(2)
    print("processing...\n")
    
    name=input("Enter Student Name: ")
    id=int(input("ID: "))
    time.sleep(2)
    print("Removing...")
    time.sleep(3)
    print("Successfully Removed\n")
    exit()
    
if option == 4:
    time.sleep(2)
    print("Please wait...")
    print("Thanks for using!")
    exit()
    
if option != menu:
	print("ERROR!")
	exit()
          
if option == 1:
    time.sleep(2)
user = input("Username: ")
pss = input("Password: ")
time.sleep(2)
print("Please wait...")
time.sleep(2)
    
for x in range(len(userInfo)):
    if user == userInfo[x] and pss == passInfo[x]:
        print("Welcome")
        break
else:
    print("Invalid")
    done()
    
