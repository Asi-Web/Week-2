## Asiwome Agbleze
## CMSC 111/1
## Spring 2026 -Login_system.py

# This would store the correct login credentials
correct_username = "admin"
correct_password = "password123"

# User would answer their username and password
username = input("Enter username: ")
password = input("Enter password: ")

# 'And' operator makes sure BOTH conditions are true
# Login is successful only if the username AND password both match
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")    