
"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:
Example
"""

def my_function():
  print("Hello from a function")

# To call a function, use the function name followed by parenthesis

my_function()

print ("-------------------------------")

"""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

Example
"""
def my_function(fname):
  print("Griffin's Family is here:" + "  " + fname + " Griffin")

my_function("Peter")
my_function("Meg")
my_function("Chris")
my_function("Stewie")
my_function("Brian")
my_function("Lois")

print ("-------------------------------")
print ("-------------------------------")
print ("-------------------------------")
print ("-------------------------------")
