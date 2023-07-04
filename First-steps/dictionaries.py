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

"""
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

Example
Check if "model" is present in the dictionary:
"""

thisdictTwo = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdictTwo:
  print("Yes, 'model' is one of the keys in the thisdictTwo dictionary")

print("--------------------------------------")

"""
Change Values
You can change the value of a specific item by referring to its key name:

Example
Change the "year" to 2018:

"""

thisdictThree = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictThree["year"] = 2018
print(thisdictThree)

"""
Update Dictionary
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example
Update the "year" of the car by using the update() method:

"""

thisdictFour = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictFour.update({"year": 2020})

print(thisdictFour)

print("--------------------------------------")

"""
Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

Example

"""
thisdictFive = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictFive["color"] = "blue"
print(thisdictFive)

"""
Update Dictionary
The update() method will update the dictionary with the items from a given argument.
If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example
Add a color item to the dictionary by using the update() method:

"""

thisdictSix = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictSix.update({"color": "red"})
print(thisdictSix)

print("--------------------------------------")

# The pop() method removes the item with the specified key name:

thisdictEight = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictEight.pop("model")
print(thisdictEight)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdictNeun = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red"
}
thisdictNeun.popitem()
print(thisdictNeun)

print("--------------------------------------")

# The del keyword removes the item with the specified key name:

thisdictTen = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdictTen["model"]
print(thisdictTen)

# The del keyword can also delete the dictionary completely:

thisdictEl = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdictEl
# print(thisdictEl) #this will cause an error because "thisdict" no longer exists.


print("--------------------------------------")

# The clear() method empties the dictionary:

thisdictTwelve = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictTwelve.clear()
print(thisdictTwelve, "This is an empty dictionary")

print("--------------------------------------")

"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example
Print all key names in the dictionary, one by one:

"""
print("----key names---")

thisdictLoop = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red"
}

for x in thisdictLoop:
  print(x)

print("----values name---")
"""
Example
Print all values in the dictionary, one by one:
"""

for y in thisdictLoop:
  print(thisdictLoop[y])

print("----values name---")

"""
Example
You can also use the values() method to return values of a dictionary:
"""

for z in thisdictLoop.values():
  print(z)


print("----keys of dict---")
"""
Example
You can use the keys() method to return the keys of a dictionary:
"""

for i in thisdict.keys():
  print(i)


print("----keys and valuies---")
"""
Example
Loop through both keys and values, by using the items() method:
"""

for e, f in thisdict.items():
  print(e, f)

print("--------------------------------------")

"""
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1,
because: dict2 will only be a reference to dict1,
and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Example
Make a copy of a dictionary with the copy() method:
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


"""
Another way to make a copy is to use the built-in function dict().

Example
Make a copy of a dictionary with the dict() function:
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydictTwo = dict(thisdict)
print(mydictTwo)

print("--------------------------------------")

"""
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

Example
Create a dictionary that contain three dictionaries:
"""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

print("---")

"""
Or, if you want to add three dictionaries into a new dictionary:

Example
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
"""

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamilyTwo = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamilyTwo)

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
