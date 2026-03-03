## Asiwome Agbleze
## CMSC 111/1
## Spring 2026 -perimeter_of_rectangle.py

# This would calculate the perimeter of a rectangle using length and width

# Ask the user for the length of the rectangle
length_input = input("Enter the length of the rectangle: ")

# Ask the user for the width of the rectangle
width_input = input("Ener the width of the rectangle: ")

# Convert both values from strings to floats
length = float(length_input)
width = float(width_input)

# Calculate  the perimeter using the formula 2 * (length + width)
perimeter = 2 * (length + width)

# Display the result as a float with a clear message
print("The perimeter of the rectangle is", perimeter)