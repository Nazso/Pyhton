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

"""
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

Example
Convert from Python to JSON:
"""

# a Python object (dict):
xx = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
yy = json.dumps(xx)

# the result is a JSON string:
print(yy)

print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
