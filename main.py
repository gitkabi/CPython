# Strings
# You can display a string literal with the print() function
print('Hello Kabi')
print("Hello Kabi")

# Assign String to a Variable
a = "Hello Kabi"
print(a)

# Multiline Strings
x = """My name is Abhishek Kabi and I love Python.
I also love working at Prexel."""
print(x)

x = '''My name is Abhishek Kabi and I love Python. 
I also love working at Prexel.''' # Single quotes
print(x)

# Strings are Arrays
x = "Hello Kabi"
print(x[0], x[1], x[2], x[3], x[4], x[5])

# Looping Through a String
for x in "Prexel ":
    print(x)
for y in "Abhishek":
    print(y)

# String Length
z = "Python"
print(len(z))

a = "Prexel"
print(len(a))

# Check String
txt = "Your name is Karthik"
print("name" in txt)
print("Abhishek" in txt)
print(len(txt))

# Use it in an if statement:
txt = "I love Python"
if "Python" in txt:
    print("Yes, 'Python' is present.")

# Check if NOT
txt = "I love Python"
print("Prexel" not in txt)

# # Use it in an if statement:
txt = "I love Python"
if "Python" not in txt:
    print("No, 'Python' is not present")

# Slicing Strings
a = "I love Python"
print(a[2:6])

# Slice From the Start
b = "My name is Abhishek"
print(b[:15])

# Slice To the End
x = "Prexel is love"
print(x[10:])

# Negative Indexing
y = "Love your soul"
print(y[-5:-1])

# Modify Strings (Uppercase)
a = "I love Python"
print(a.upper())

#Lowercase
a = "I LOVE PYTHON"
print(a.lower())

# Remove Whitespace
a = "I love python"
print(a.strip())

# Replace String
a = "I love python"
print(a.replace("I", "X"))

# Split String
a = "I love Python"
print(a.split("y"))

# String Concatenation
x = "Abhishek "
y = "Kabi"
z = x + y
print(z)

# Format - Strings
age = "28"
txt = ("My age is " + age)
print(txt)

age = 28
txt = "My name is Kabi, and I am {}"
print(txt.format(age))

road = "Gotri"
City = "Vadodara"
State = "Gujarat"
txt = "My address will be {} road, {} city, {} state"
print(txt.format(road, City,State))

# Using index numbers
price = 50
quantity = 2
item = 1
txt = "I brought {2} item for the price of {0} having a quantity of {1}"
print(txt.format(price, quantity, item))

# Escape Characters (Presented by a Backlash)
txt = "We are Prexelites from \"around\" the Globe."
print(txt)

# Escape characters using index numbers
quantity = 10
price = 500
txt = "The most amazing fruit is \"Mango\" bought at {0} rupees having a quantity of {1}."
print(txt.format(price, quantity))

# Method	        Description
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	         Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning

