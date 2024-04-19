# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and
# Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
import l

list = ["Apple", "Banana", "Cherry"]
print(list)

# To determine length list
City = ["People", "Space", "Shops", "Schools", "Colleges"]
print(len(City))

# List Items - Data Types
list1 = ["People"], ["Space"], ["Schools"]
list2 = [1, 2, 3, 4]
list3 = [True, False, True]
print(list1, list2, list3)

list1 = ["People", 100, True]
print(list1)

# What is the data type of a list?
numbers = [1, 2, 3, 4]
print(type(numbers))

# Accessing Items
list = ["People", 100, True]
print(list[0])

# Negative indexing means start from the end
list = ["People", 100, True]
print(list[-2])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:6])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists
list = ["Apple", "Banana", "Cherry"]
if "Apple" in list:
    print("Yes, 'Apple' is in the fruits list")

# Change Item Value
list = ["Apple", "Banana", "Cherry"]
list[1] = ["Blueberry"]
print(list)

TimeZones = ["EST", "CST", "MST", "PST", "QST"]
TimeZones[4] = ["HST"]
print(TimeZones)

# Change a Range of Item Values
list = ["Apple", "Banana", "Cherry", "Orange", "Kiwi"]
list[1:3] = ["Blueberry", "Mango"]
print(list)

# Change the second value by replacing it with two new values:
list = ["apple", "banana", "cherry"]
list[1:2] = ["blackcurrant", "watermelon", "Cranberry"]
print(list)

# Insert "watermelon" as the third item:
list = ["apple", "banana", "cherry"]
list.insert(2, 'watermelon')
print(list)

# Append Items
list = ["apple", "Banana", "Cherry"]
list.append("Mango")
print(list)

list = ["Apple", "Banana", "Cherry"]
list.insert(0, "Mango")
print(list)

list = ["Apple", "Banana", "Cherry"]
tropical = ["Mango", "Watermelon", "Grapes"]
list.extend(tropical)
print(list)

list = [1, 2, 3, 4, 5]
numbers = [6, 7, 8, 9, 10]
list.extend(numbers)
print(list)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
list = ["Apple", "Banana", "Cherry"]
tuple = ["Mango", "Watermelon", "Grapes"]
list.extend(tuple)
print(list)

# Remove List Items
list = ["Apple", "Banana", "Mango"]
list.remove("Banana")
print(list)

# Remove Specified Index
list = ["Apple", "Cherry", "Mango"]
list.pop(1) # If you do not specify the index, the pop() method removes the last item.
print(list)

list = ["Apple", "Cherry", "Mango"]
del list[0] # The del keyword also removes the specified index:
print(list)

list = [1, 2, 3, 4, 5]
del list # The del keyword can also delete the list completely.

list = ["Apple", "Banana", "Mango"]
list.clear() # The clear() method empties the list.
print(list)

# Loop through a list
list = [1, 2, 3, 4, 5]
for x in list:
    print(x)

# Loop Through the Index Numbers
list = [1, 2, 3]
for i in range(len(list)):
    print(list)

name = ["Abhi", "Karthik", "Sourav"]
for i in range(len(name)):
    print(name)
    print(name[i]) # Prints all items by referring to their index number

# Using a While Loop
list = ["apple", "banana", "cherry"]
i = 0
while i < len(list):
    print(list[i])
    i = i + 1

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(Numbers):
    print(Numbers[i])
    i = i + 2

Names = ["Abhi", "Prem", "Ankur", "Vishal", "Deepal"]
i = 1
while i < len(Names):
    print(Names[i])
    i = i + 1

alpha = ["A", "B", "C", "D", "E"]
i = 0
while i < (len(alpha)):
    print(alpha[i])
    i = i + 1

# Looping Using List Comprehension
list = [1, 2, 3, 4, 5]
[print (x) for x in list]

# List Comprehension
fruits = ["apple", "Mango", "Apricot", "Grapes", "Almond"]
newlist = [x for x in fruits if "a" not in x]
print(newlist)

Alpha = ["A", "B", "A", "A", "C"]
newlist = [x for x in Alpha if "A" in x]
print(newlist)

# Syntax - newlist = [expression for item in iterable if condition == True]
fruits = ["Apple", "Mango", "Apricot", "Grapes", "Almond"]
list = [x for x in fruits if x!= "Apple"] # with If statement
print(list)

fruits = ["Apple", "Mango", "Apricot", "Grapes", "Almond"] # with no if statement
list = [x for x in fruits]
print(list)

list = [x for x in range(10)] # with range function
print(list)

list = [x for x in range(10) if x < 8] # with a condition
print(list)

# Set the values in the new list to upper case:
fruits = ["Apple", "Mango", "Apricot", "Grapes", "Almond"]
list = [x.upper() for x in fruits]
print(list)

# Set the values in the new list to lower case:
Names = ["Abhi", "Prem", "Ankur", "Vishal", "Deepal"]
list = [x.lower() for x in Names]
print(list)

Names = ["Abhi", "Prem", "Ankur", "Vishal", "Deepal"]
list = ["Prexelites" for x in fruits]
print(list)

# The expression in the example above says:
fruits = ["Apple", "Mango", "Apricot", "Grapes", "Almond"]
list = [x if x!= 'Apple' else "Blueberry" for x in fruits] # "Return the item if it is not Apple, if it is Apple return orange".
print(list)

Names = ["Abhi", "Prem", "Ankur", "Vishal", "Deepal"]
list = [x if x!= "Abhi" else "Prexelite" for x in Names]
print(list)

list = [x if x!= 1 else "?" for x in range(10)]
print(list)

# Sort List Alphanumerically
list = ["Apple", "Mango", "Apricot", "Grapes", "Almond"]
list.sort()
print(list)

# Sort List in reverse
list = [10, 5, 50, 90, 40, 30]
list.sort(reverse = True)
print(list)

# Case Insensitive Sort
list = ["kiwi", "Orange", "Mango", "apricot"]
list.sort()
print(list)

# Perform a case-insensitive sort of the list:
list = ["kiwi", "Orange", "Mango", "apricot"]
list.sort(key = str.lower)
print(list )

# Reverse Order
list = ["kiwi", "Orange", "Mango", "apricot"]
# list.sort(reverse)
print(list)

list = ["kiwi", "apricot"]
mylist = list.copy()
print(mylist)

# Join Two Lists
list1 = [1 + 2 + 3 + 4]
list2 = [1 + 9]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = [1 + 2 + 3 + 4]
list2 = [1 + 9]

for x in list2:
    list1.append(x)
    print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1 = [1 + 2 + 3 + 4]
list2 = [1 + 9]

for x in list2:
    list1.extend(list2)
    print(list1)

# Python has a set of built-in methods that you can use on lists.
# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list


