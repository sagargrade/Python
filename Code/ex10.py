# Use of escape character \
# \t is used to provide tab space
tabby_cat = "\tI'm tabbed in."
# \n is used to provide new line
persian_cat = "I'm split\non a line."
# \\ is used to keep \ in the string
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

another_cat = '''
Hi This is another cat.
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(another_cat)

print(f"There are many cats. \nThere are list of values which need to be taken care. \n{fat_cat}")

# \\ -> Backslash (\)
# \' -> Single Quote
# \" -> Double Quote
# \a -> ASCII Bel
# \b -> ASCII Backspace
# \f -> ASCII formfeed
# \n -> ASCII linefeed
# \N{name} -> Character named name in unicode database
# \r -> Carriage Return
# \t -> Horizontal Tab
# \uxxxx -> Character with 16 bit hex value xxxx
# \Uxxxxxxxx -> Character with 32 bit hex value xxxxxxxx
# \v -> ASCII Vertical Tab
# \ooo -> Character with octal value ooo
# \xhh -> Character with hex value hh
