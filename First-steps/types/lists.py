thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

listDiff = ["abc", 34, True, 40, "male"]

print(listDiff)

print(type(listDiff))

print('-------------------------')

# It is also possible to use the list() constructor when creating a new list.

newlist = list(("apple", "banana", "cherry"))   # note the double round-brackets
print(newlist)

print('-------------------------')

"""
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

print('-------------------------')

"""
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
The search will start at index 2 (included) and end at index 5 (not included).
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print('-------------------------')

"""
By leaving out the start value, the range will start at the first item
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print('-------------------------')

"""
By leaving out the end value, the range will go on to the end of the list
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print('-------------------------')

"""
Specify negative indexes if you want to start the search from the end of the list

This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print('-------------------------')

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print('-------------------------')

# change the second item of list!

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print('-------------------------')

"""
To change the value of items within a specific range, 
define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[3:5] = ["something", "delicious"]
print(thislist)

print('-------------------------')

"""
If you insert more items than you replace,
the new items will be inserted where you specified,
and the remaining items will move accordingly

Change the second value by replacing it with two new values
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print('-------------------------')

"""
If you insert less items than you replace,
the new items will be inserted where you specified,
and the remaining items will move accordingly

Change the second and third value by replacing it with one value
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print('-------------------------')

"""
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print('-------------------------')
"""
To add an item to the end of the list, use the append() method
"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print('-------------------------')

"""
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print('-------------------------')

"""
To append elements from another list to the current list, use the extend() method.
"""

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print('-------------------------')

"""
The remove() method removes the specified item.
"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""
The pop() method removes the specified index.
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)

"""
If you do not specify the index, the pop() method removes the last item.
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

"""
The del keyword also removes the specified index.
The del keyword can also delete the list completely.
"""

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist # clompletely list is deleted


"""
The clear() method empties the list.

The list still remains, but it has no content.
"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print('-------------------------')

"""
Loops
"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print('-----------------')

"""
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
"""

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print('-------------------------')

"""
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
"""

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("------")

"""
List Comprehension offers the shortest syntax for looping through lists:
"""

thislist = ["apple", "banana", "cherry", "melone"]
[print(x) for x in thislist]


print('-------------------------')

"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#same list just one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
newlistOne = [x for x in fruits if x != 'apple']

print(newlist)
print(newlistOne)

print('-------------------------')

#Iterable

newlist = [x for x in range(10)]
print(newlist)

newlistTwo = [x for x in range(10) if x < 5]
newlistThree = [x for x in range(10) if x > 5]
print(newlistTwo)
print(newlistThree)

print('-------------------------')

"""
List objects have a sort() method that will sort the list alphanumerically, ascending, by default
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print('-------------------------')

"""
To sort descending, use the keyword argument reverse = True
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

print('-------------------------')

"""
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first)
Sort the list based on how close the number is to 50
"""

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print('-------------------------')

"""
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function
Perform a case-insensitive sort of the list
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print('-------------------------')

"""
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print('-------------------------')

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["Car", "Plane", "Bus"]
mylist = list(thislist)
print(mylist)

print('-------------------------')

#join (concatenate) lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


print('-------------------------')

"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

print('-------------------------')
print('-------------------------')
