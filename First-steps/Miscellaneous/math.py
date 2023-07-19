"""
Python Math
Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:

ExampleGet your own Python Server
"""

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

print("-------------------abs--------------------")

"""
The abs() function returns the absolute (positive) value of the specified number:

Example
"""

x = abs(-7.25)

print(x)

print("--------------------pow-------------------")

"""
The pow(x, y) function returns the value of x to the power of y (xy).

Example
Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

"""

x = pow(4, 3)
y = pow(5, 10)
z = pow(2, 8)

print(x)
print(y)
print(z)

print("---------------------------------------")

"""
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

import math
When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:

Example
"""
import math

x = math.sqrt(64)

print(x)

print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
