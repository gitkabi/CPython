# Tuples
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
tuple = ("X", "Y", "Z")
print(tuple)

# Tuple Length
tuple = ("Banana", "Apple", "Mango")
print(len(tuple))

tuple = ("Apple",)  # To create a tuple with only one item, you have to add a comma after the item,
                    # otherwise Python will not recognize it as a tuple.
print(type(tuple))

# Tuple Items - Data Types
tuple1 = ("Banana", "Cherry", "Mango")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("True", "False", "True")
print(tuple1, tuple2, tuple3)

tuple = ("Kabi", 10, "True")
print(tuple)

# Access Tuple Items
tuple = ("banana", "Cherry", "Mango")
print(tuple[1])
print(tuple[1:3])

# Negative Indexing
tuple = ("banana", "Cherry", "Mango")
print(tuple[-1])

# Range of Indexes
tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[2:7])

# Check if Item Exists
tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "watermelon" in tuple:
    print("Yes, 'mango' is present in fruits")
else:
    print("No, the fruit is not present in the list")

# Change Tuple Values
x = ("banana", "Cherry", "Mango")
y = list(x)
y[1] = "kiwi"
x = list(y)
print(x)

# Add Items
tuple = ("banana", "Cherry", "Mango") # First way
y = list(tuple)
y.append("Kiwi")
print(y)

tuple = ("banana", "Cherry", "Mango") # Second way
y = ("orange",)
tuple += y
print(tuple)

# Remove Items
tuple = ("banana", "Cherry", "Mango")
y = list(tuple)
y.remove("banana",)
tuple = y
print(tuple)

# Deleting the tuple
tuple = ("banana", "Cherry", "Mango")
del tuple

# Unpack Tuples
fruits = ("banana", "Cherry", "Grapes") # this line itself is a packed tuple
(yellow, red, black) = fruits
print(yellow, red, black)

# Using Asterisk*
fruits = ("banana", "Grapes", "Cherry", "strawberry", "raspberry")
(yellow, black, *red) = fruits
print(yellow, black, red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropical, red) = fruits
print(green, tropical, red)

# Loop Through a Tuple
tuple = ("apple", "mango", "papaya", "pineapple", "cherry")
for x in tuple:
    print(x)

# Loop Through the Index Numbers
tuple = ("apple", "mango", "papaya", "pineapple", "cherry")
for i in range(len(tuple)):
    print(tuple[i])

# Using a While Loop
tuple = ("apple", "mango", "papaya", "pineapple", "cherry")
i = 1
while i < len(tuple):
    print(tuple[i])
    i = i + 1

# Add two tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply two tuples
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
tuple = fruits * 2
print(tuple)

# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

