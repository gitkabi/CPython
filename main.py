# Boolean Values
print(10 > 9)
print(10 < 9)
print(10 == 9)

# Print a message based on whether the condition is True or False:
a = 40
b = 10
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(1))

# Evaluate two variables:
x = 10
y = "Prexel"
print(bool(x))
print(bool(y))

bool("Kabi")
bool("123")
bool(["mango", "grapes", "orange"])
print(bool)

# Functions can Return a Boolean
def myfunction():
    return False
print(myfunction())

# Print "YES!" if the function returns True, otherwise print "NO!":


def myfunction():
    return True


if myfunction():
    print("Yes")
else:
    print("No")

# isinstance() function, which can be used to determine if an object is of a certain data type:
x = 100
print(isinstance(x, int))