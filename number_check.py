## Asiwome Agbleze
## CMSC 111/1
## Spring 2026 - number_check.py

#Ask the user to enter a number and store it as text
user_input = input("Enter a number: ")

# Conver the input string to a floast so we can compare its value
number =float(user_input)

# If the number is greater than zero, it is positive
if number > 0:
    print("The number is positive.")

# elif checks another condition only if the first onw was false
elif number < 0:
    print("The number is negative.")

# else runs when none of the above conditions are true (so the number must be zero)
else:
    print("The number is zero.") 
       