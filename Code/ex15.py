# Import argv feature from sys module
from sys import argv
# Split up argv into script and filename
script, filename = argv
# Open file. It Creates File Object
txt = open(filename)
# Print the name of the file which you opened
print(f"Here's your file {filename}:")
# Print the read content of file.
print(txt.read())
# Close the file
txt.close()
# Get the file name again
print("Type the filename again:")
file_again = input("> ")
# Open the file
txt_again = open(file_again)
# Read the content of file and print the content of file.
print(txt_again.read())
# Close the file
txt_again.close()
