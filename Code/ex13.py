from sys import argv
# sys -> module
# argv -> feature of module
# argv is argument variable
script, first, second, third = argv
#
print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your thrid variable is:", third)

# Execution :
#
# C:\Users\sgd8w23\Desktop\Learn\Python\Code>python ex13.py 1st 2nd 3rd
# This script is called: ex13.py
# Your first variable is: 1st
# Your second variable is: 2nd
# Your thrid variable is: 3rd

value = input("do you want to enter any other value? ")
print("Your last variable is:",value)
