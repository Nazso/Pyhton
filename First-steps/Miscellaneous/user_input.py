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

username = input("Enter username:")
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
