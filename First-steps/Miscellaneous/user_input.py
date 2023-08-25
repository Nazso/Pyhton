"""
User Input
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

Python 2.7 uses the raw_input() method.

The following example asks for the username, and when you entered the username, it gets printed on the screen:

Python 3.6
"""

#username = input("Enter username:")
#print("Username is: " + username)

# Python stops executing when it comes to the input() function, and continues when the user has given some input.

print("-------------------------------string format()--------------------------------")

# String formatting
"""
To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

ExampleGet your own Python Server
Add a placeholder where you want to display the price:
"""

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

"""
You can add parameters inside the curly brackets to specify how to convert the value:

Example
Format the price to be displayed as a number with two decimals:

"""
txt = "The price is {:.2f} dollars"
print(txt.format(price))

print("--------------------------Multiple values-----------------------")

"""
Multiple Values
If you want to use more values, just add more values to the format() method:

"""

# print(txt.format(price, itemno, count))

"""
And add more placeholders:

Example
"""

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("-----------------------Index numbers--------------------")

"""
Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

Example

"""
quantity = 3
itemno = 567
price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
myorder = "I want {1} pieces of item number {2} for {0:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""
Also, if you want to refer to the same value more than once, use the index number:

Example
"""

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print("-----------------------Named indexes--------------------")

"""
Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

Example
"""

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

