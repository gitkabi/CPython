# Variables
myvar = "Kabi"
my_var = "Kabi"
_my_var = "Kabi"
myVar = "Kabi"
MYVAR = "Kabi"
myvar19 = "Kabi"

print(myvar)
print(my_var)
print(_my_var)
print(MYVAR)
print(myvar19)

# Camel Case
myVariableName = "Kabi"
print(myVariableName)

# Pascal Case
MyVariableName = "Kabi"
print(MyVariableName)

# Snake Case
my_variable_name = "Kabi"
print(my_variable_name)

# Multiple Variables
x, y, z = "Mango", "Grapes", "Blueberry"
print(x, y, z)

# One Value to Multiple Variables
x = y = z = "Mango"
print(x, y, z)

# Unpack a Collection
fruits = ("mango", "grapes", "Blueberry")
x, y, z = fruits
print(x, y, z)

# Output Variables
x = "Prexel is an awesome place to work"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Prexel is "
y = "an awesome place "
z = "to work"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:
x = 10
y = 90
print(x + y)

# Global Variables
x = "awesome"


def myfunc():
    print("Prexel is " + x)


myfunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Prexel is " + x)


myfunc()

print("Prexel is " + x)


# The global Keyword


def myfunc():
    global x
    x = "fantastic"

# Also, use the global keyword if you want to change a global variable inside a function
x = "Awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Prexel is " +x)



