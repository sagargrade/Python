# Declare a variable of types of people and assign value
types_of_people = 10
# Create a format string "f string" using valiable types of people and store it
x = f"There are {types_of_people} types of people."
# Declare two variables one for binary another one for dont
binary = "binary"
do_not = "don't"
# Create a fstring using binary and do_not variable and store it
y = f"Those who know {binary} and those who {do_not}"
# Print created f strings
print(x)
print(y)
# Print fstring by taking variables which holdd fstrings
print(f"I said: {x}")
print(f"I also said: '{y}'")
# Create a variable to hold binary value and another variable with string having
# a place holder a variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# Use format function to populate variable value in place folder of string.
print(joke_evaluation.format(hilarious))
# Create two variable with strings0
w = "This is the left side of..."
e = "a string with a right side."
# Concatenate both the strings.
print(w + e)
