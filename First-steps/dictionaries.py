"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


"""
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(thisdict["model"])


"""
There is also a method called get() that will give you the same result:
"""

x = thisdict.get("year")
print(x)

print("--------------------------------------")

"""
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

Example
Duplicate values will overwrite existing values:
"""

thisdictOne = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "color": "blue"
}
print(thisdictOne)
print(len(thisdictOne))

print("--------------------------------------")

x = thisdictOne.keys()

print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

y = car.values()
print(y)

car["year"] = 2020

print(y) #after the change


print("--------------------------------------")

# Add a new item to the original dictionary, and see that the values list gets updated as well:


x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

print("--------------------------------------")

"""
The items() method will return each item in a dictionary, as tuples in a list.

Example
Get a list of the key:value pairs
"""

x = thisdict.items()
print(x)


z= car.items()
print(z) #before the change

car["year"] = 2021
print(z) #after the change

print("--------------------------------------")
print("--------------------------------------")
