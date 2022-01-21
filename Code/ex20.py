from sys import argv

script, input_file = argv
# Function to print all lines of file.
def print_all(f):
    print(f.read())
# Function to keep position at top of the file
def rewind(f):
    f.seek(0) # Seek function will change the position of file
# Function to print one line
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Open the file and store file object into variable
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
