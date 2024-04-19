# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 2024
}
print(dict)

# Print the "brand" value of the dictionary:
dict = {
    "brand": "Ferrari",
    "model": "Roma",
    "year": "2024"
}
print(dict["brand"])
print(len(dict))  # To determine how many items a dictionary has, use the len() function

# The values in dictionary items can be of any data type:
dict = {
    "Brand": "Ferrari",
    "electric": "True",
    "Model": "Roma",
    "Color": ["Red", "Blue", "White"]
}
print(dict)
print(type(dict))  # Prints the data type of dictionary

# Python Collections (Arrays)
# List is a collection which is ordered and changeable.                 Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable.              Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and indexed.   No duplicate members.
# Dictionary is a collection which is ordered** and changeable.         No duplicate members.

# Accessing Items
dict = {
    "Name": "Abhi",
    "Age": "29",
    "Gender": "Male",
    "Nationality": "Indian"
}
print(dict["Nationality"])  # 1st way to call a value
x = dict["Nationality"]  # 2nd way to call a value
x = dict.get("Nationality")  # 3rd way to call a value

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys() # The keys() method will return a list of all the keys in the dictionary.
print(x)

car["color"] = "Red"
print(x)

# Get Values
dict = {
    "Name": "Abhi",
    "Age": "29",
    "Gender": "Male",
    "Nationality": "Indian"
}
x = dict.values() # The values() method will return a list of all the values in the dictionary.
print(x)

dict["Color"] = "White"
print(x)

# Get Items
dict = {
    "Name": "Abhi",
    "Age": "29",
    "Gender": "Male",
    "Nationality": "Indian"
}
x = dict.items() # The items() method will return each item in a dictionary, as tuples in a list.
print(x)

dict["Color"] = "White"
print(x)

# Check if Key Exists
# Check if "Age" is present in the dictionary:
dict = {
    "Name": "Abhi",
    "Age": "28",
    "Gender": "Male"
}
if "Age" in dict:
    print("Yes, Age is just a number")
else:
    print("Please call the right thing from the dict")

# Change Values
dict = {
    "Name": "Abhi",
    "Age": "28",
    "Gender": "Male"
}
dict["Age"] = 29
print(dict)

# Update Dictionary
# Update the "year" of the car by using the update() method:
dict = {
    "Name": "Abhi",
    "Age": "28",
    "Gender": "Male"
}
dict.update({"Age":29})
print(dict)

# Adding Items
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["color"] = "red"
print(dict)

# Update Items
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.update({"color": "red"} | {"Years used": "05"} | {"Wheels": "Alloy"}) # The update() method will update the dictionary with the items from a given argument.
print(dict)

# Rmoving Items by 3 ways:
# Pop() method:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.pop("year") # The pop() method removes the item with the specified key name
dict.popitem() # The popitem() method removes the last inserted item
print(dict)

# clr() method:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# dict.clr() # The clear() method empties the dictionary #(Remove the # at the start to make it run)
print(dict)

# del() method:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del dict["year"] # The del keyword removes the item with the specified key name
del dict # The del keyword can also delete the dictionary completely
print(dict)

# Loop Dictionaries
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}
for x in dict:
    print(x) # Print all key names in the dictionary

for x in dict:
    print(dict[x]) # Print all values in the dictionary

for x in dict.values(): # use the values() method to return values of a dictionary
    print(x)

for x in dict.keys(): # use the keys() method to return the keys of a dictionary
    print(x)

# Loop through both keys and values, by using the items() method:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}
# for x,y in dict.items():
#    print(x,y)

# Copy Dictionaries
# Make a copy of a dictionary with the copy() method:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}
# mydict = dict.copy()
# print(mydict)

# Make a copy of a dictionary with the dict() function:
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# mydict = dict(dict1)
# print(mydict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
child1 = {
    "Name": "Miku",
    "Age": 22
}
child2 = {
    "Name": "Chiku",
    "Age": 29
}
family = {
    "child1" : child1,
    "child2" : child2,
}
print(family)

# Access Items in Nested Dictionaries
child1 = {
    "Name": "Miku",
    "Age": 22
}
child2 = {
    "Name": "Chiku",
    "Age": 29
}
family = {
    "child1" : child1,
    "child2" : child2,
}
#print(family["child2"]["Name"]) # Prints the name of child 2
#print(family["child1"]["Age"]) # Prints the age of child 1

for x, obj in family():
    print(x)

for y in obj:
    print(y + ":", obj[y])

# Method	                Description
# clear()	                Removes all the elements from the dictionary
# copy()	                Returns a copy of the dictionary
# fromkeys()	            Returns a dictionary with the specified keys and value
# get()	                    Returns the value of the specified key
# items()	                Returns a list containing a tuple for each key value pair
# keys()	                Returns a list containing the dictionary's keys
# pop()	                    Removes the element with the specified key
# popitem()	                Removes the last inserted key-value pair
# setdefault()	            Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	                Updates the dictionary with the specified key-value pairs
# values()	                Returns a list of all the values in the dictionary