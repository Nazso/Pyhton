
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

# Arguments are often shortened to args in Python documentations.

print ("-------------------------------")

"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

Example
This function expects 2 arguments, and gets 2 arguments:
"""

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Glenn", "Quagmire")

# If you try to call the function with 1 or 3 arguments, you will get an error:

print ("-------------------------------")

"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly

Example
If the number of arguments is unknown, add a * before the parameter name
"""

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Chris", "Meg", "Stewie")

# Arbitrary Arguments are often shortened to *args in Python documentations.

print ("-------------------------------")

"""
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

Example
"""

def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

print ("-------------------------------")

"""
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example
"""

def my_function(country = "Hungary"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print ("-------------------------------")

"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

Example
"""

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print ("-------------------------------")

"""
Return Values
To let a function return a value, use the return statement:

Example
"""

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print ("-------------------------------")

"""
The pass Statement
function definitions cannot be empty,
but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

Example
"""

def myfunction():
  pass

print ("-------------------------------")

"""
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept.
It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function
which never terminates, or one that uses excess amounts of memory or processor power.
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
We use the k variable as the data, which decrements (-1) every time we recurse.
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works,
best way to find out is by testing and modifying it.

Example
Recursion Example
"""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
# tri_recursion(45)
tri_recursion(10)


print ("-------------------------------")

"""
Python Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:

Example
Add 10 to argument a, and return the result:
"""

x = lambda a : a + 10
print(x(5))

print ("-------------------------------")

"""
Lambda functions can take any number of arguments:

Example
Multiply argument a with argument b and return the result:
"""

x = lambda a, b : a * b
print(x(5, 6))


# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print ("-------------------------------")

"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:
"""

# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Or, use the same function definition to make a function that always triples the number you send in:


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(10))


# Or, use the same function definition to make both functions, in the same program:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(20))
print(mytripler(30))


# Use lambda functions when an anonymous function is required for a short period of time.

print ("-------------------------------")
print ("-------------------------------")
