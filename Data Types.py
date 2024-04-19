# Getting the Data Type
# Print the data type of the variable x:

x = 5
print(type(x))

# Setting the Data Type
# x = str("Hello World")	                        #str
# x = int(20)	                                    #int
# x = float(20.5)	                                #float
# x = complex(1j)	                                #complex
# x = list[("apple", "banana", "cherry")]	        #list
# x = tuple(("apple", "banana", "cherry"))          #tuple
# x = range(6)	                                    #range
# x = dict(name="John", age=36)	                    #dict
# x = set{"apple", "banana", "cherry"}	            #set
# x = frozenset{"apple", "banana", "cherry"}	    #frozenset
# x = bool(5)	                                    #bool
# x = bytes(5)	                                    #bytes
# x = bytearray(5)	                                #bytearray
# x = memoryview(bytes(5))	                        #memoryview

# Python Numbers
# int
# float
# complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# convert from int to float:
x = float(1)
print(x)
print(type(x))

# convert from float to int:
y = int(2.8)
print(y)
print(type(y))

# convert from int to complex:
z = complex(1)
print(z)
print(type(z))
# Note: You cannot convert complex numbers into another number type.

# Random Number
import random
print(random.randrange(1, 10))

# Python Casting
# Casting in python is therefore done using constructor functions:
# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
x = int(1)
y = int(3.5)
z = int("3")
print(x, y, z)

# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
x = float(1.4)
y = float(4)
z = float("9")
print(x, y, z)

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
x = str(1.0)
y = str(4)
z = str("s1")
print(x, y, z)
