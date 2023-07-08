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
print("-------------------------")
print("-------------------------")
