"""
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
"""

"""
Sets are unordered, so you cannot be sure in which order the items will appear.

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

"""
The values True and 1 are considered the same value in sets, and are treated as duplicates
"""

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

print("--------------------------------------")

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

setOne = {"abc", 34, True, 40, "male"}
print(setOne)


print("--------------------------------------")

myset = {"apple", "banana", "cherry"}
print(type(myset))

print("--------------------------------------")

# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
