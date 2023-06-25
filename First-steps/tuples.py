"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""

"""
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print('-------------------------')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print('-------------------------')

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print('-------------------------')

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

print('-------------------------')

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print('-------------------------')

"""
It is also possible to use the tuple() constructor to make a tuple.
"""

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
