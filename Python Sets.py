# A set is a collection which is unordered, unchangeable*, and unindexed.
set = {"Prem", "Abhi", "Prexel"}
print(set)

set = {"apple", "banana", "cherry", True, 1, 2}
print(set)
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

set = {"apple", "banana", "cherry", False, True, 0}
print(set)
# False and 0 is considered the same value

set = {"Prem", "Abhi", "Prexel"}
print(len(set))

#  Data Types
set = {"abc", 34, True, 40, "male"}
print(set)

set = {"apple", "banana", "cherry"}
print(type(set))

# Access Set Items
set = {"apple", "banana", "cherry"} # Loop through the set, and print the values:

for x in set:
    print(x)

# Check if "banana" is present or not in the set:
set = {"apple", "banana", "cherry"}
print("banana" in set)
print("banana" not in set)

# Add Set Items
set = {"apple", "banana", "cherry"}
set.add("mango")
print(set)

# To add items from another set into the current set, use the update() method
set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
set.update(tropical)
print(set)

# Add Any Iterable
set = {"apple", "banana", "Cherry", "Mango"}
list = ["kiwi", "Orange"]
set.update(list)
print(set)

set = {1, 2, 3, 4, 5}
list = [6, 7, 8, 9, 10]
set.update(list)
print(set)

# Remove Set Items
set = {"apple", "banana", "cherry"}
set.remove("banana")
print(set)

set = {"apple", "banana", "cherry"}
set.discard("banana")
print(set)

set = {"apple", "banana", "cherry"}
x = set.pop()
print(x)
print(set)

set = {"apple", "banana", "cherry"}
set.clear()
print(set)

set = {"apple", "banana", "cherry"}
del set
print(set)

# Loop Sets
set = {"apple", "banana", "cherry"}
for x in set:
    print(x)

# Join Sets
# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Join set1 and set2 into a new set:
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2| set3| set4
print(myset)

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c", "d"}
y = (1, 2, 3, 4, 5)
z = x.union(y)
print(z)

# The update() method inserts the items in set2 into set1:
set1 = {1, 2, 3, 4, 5}
set2 = {"a", "b", "c"}
set1.update(set2)
print(set1)

# Intersection
# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference
# The difference() method will return a new set that will contain only the items from the first set that are
# not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "Cherry", "Banana", "Mango"}
set2 = {"apple", "Cherry", "Kiwi", "Mango"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "Cherry", "Banana", "Mango"}
set2 = {"apple", "Cherry", "Kiwi", "Mango"}
set3 = set1 ^ set2
print(set3)

# Set Methods
# Python has a set of built-in methods that you can use on sets.
#
# Method	                    Shortcut	    Description
# add()	 	                                    Adds an element to the set
# clear()	 	                                Removes all the elements from the set
# copy()	 	                                Returns a copy of the set
# difference()	                    -	        Returns a set containing the difference between two or more sets
# difference_update()	            -=	        Removes the items in this set that are also included in another, specified set
# discard()	 	                                Remove the specified item
# intersection()	                &	        Returns a set, that is the intersection of two other sets
# intersection_update()	            &=	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                            Returns whether two sets have a intersection or not
# issubset()	                    <=	        Returns whether another set contains this set or not
#  	                                <	        Returns whether all items in this set is present in other, specified set(s)
# issuperset()	                    >=	        Returns whether this set contains another set or not
#  	                                >	        Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                                    Removes an element from the set
# remove()	 	                                Removes the specified element
# symmetric_difference()	        ^	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    ^=	        Inserts the symmetric differences from this set and another
# union()	                        |	        Return a set containing the union of sets
# update()	                        |=	        Update the set with the union of this set and others
