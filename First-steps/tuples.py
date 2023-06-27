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


print('---------------------------')

"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

x = ("apple", "banana", "cherry")   # ez egy tuple
y = list(x)                         # konvertálom list-be
y[1] = "kiwi"                       # módosítom
x = tuple(y)                        # visszaalakítom tuple-é

print(x)

print('---------------------------')

"""
Since tuples are immutable, they do not have a built-in append() method,
but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple,
you can convert it into a list, add your item(s), and convert it back into a tuple.
"""

thistuple = ("apple", "banana", "cherry")
a = list(thistuple)
a.append("orange")
thistuple = tuple(a)

print(thistuple)

"""
2. Add tuple to a tuple. You are allowed to add tuples to tuples,
so if you want to add one item, (or many),
create a new tuple with the item(s), and add it to the existing tuple
"""

thistupleOne = ("apple", "banana", "cherry")
y = ("orange",)         # a vessző azért kell, mert csak így hoz létre tuple-t! E nélkül csak egy elem lesz és nem működnek dolgok.
thistupleOne += y

print(thistupleOne)

print('---------------------------')

"""
Tuples are unchangeable, so you cannot remove items from it,
but you can use the same workaround as we used for changing and adding tuple items

Convert the tuple into a list, remove "apple", and convert it back into a tuple
"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

"""
Or you can delete the tuple completely

The del keyword can delete the tuple completely
"""

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

print('---------------------------')
print('---------------------------')
print('---------------------------')
