# Import argv feature from sys package/module
from sys import argv
# Get Script name and File Name from argv
script, filename = argv
# Ask user before deleting the data
print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
# If you confirm for deletion then open the file.
print("Opening the file...")
target = open(filename, 'w')
# Use truncate() function to clean up the file.
print("Truncating the file. Goodbye!")
target.truncate()
# Now as user to enter some lines
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1 :")
line2 = input("Line 2 :")
line3 = input("Line 3 :")

print("I'm going to write these to the file.")
# Write those lines in file and add line break after each line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# Close the file.
target.close()
