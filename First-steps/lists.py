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
print('-------------------------')
print('-------------------------')