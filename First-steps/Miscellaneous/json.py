"""
Python JSON
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.
"""

# Import the json module:

import json

"""
Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.

The result will be a Python dictionary.

Example
Convert from JSON to Python:
"""

# some JSON:
x =  '{ "name":"Luke", "age":18, "city":"Tatuin"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])
print(y["age"])

print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
