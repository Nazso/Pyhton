"""
What is an Array?
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.

Access the Elements of an Array
You refer to an array element by referring to the index number.

Example
Get the value of the first array item:
"""

cars = ["Ford", "Volvo", "BMW"]
colors = ["red", "green", "blue"]
x = cars[0]
y = colors[1]
z = cars + colors
w = {"favorite car": cars[2], "favorite color":  colors[0]}

print(x)
print(y)
print(z)
print(w)


print("-------------------------")

# Modify the value of the first array item:

cars[0] = "Toyota"
print(cars)

print("-------------------------")

"""
The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

Example
Return the number of elements in the cars array:
"""

length = len(cars)

print(length)

# Note: The length of an array is always one more than the highest array index.

print("-------------------------")

"""
Looping Array Elements
You can use the for in loop to loop through all the elements of an array.

Example
Print each item in the cars array:
"""

for x in cars:
  print(x)

print("-------------------------")

"""
Adding Array Elements
You can use the append() method to add an element to an array.

Example
Add one more element to the cars array:
"""

cars.append("Honda")
print(cars)

print("-------------------------")

"""
Removing Array Elements
You can use the pop() method to remove an element from the array.

Example
Delete the second element of the cars array:
"""

cars.pop(1)
print(cars)

"""
You can also use the remove() method to remove an element from the array.

Example
Delete the element that has the value "Volvo":
"""
cars.remove("BMW")
print(cars)


# Note: The list's remove() method only removes the first occurrence of the specified value.

print("-------------------------")
