"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""

print("------If statement--------")
a = 33
b = 200
if b > a:
  print("b is greater than a")


"""
Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

If statement, without indentation (will raise an error)
"""

print("-------elif-----")

"""
Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

Example
"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

"""
In this example a is equal to b, so the first condition is not true,
but the elif condition is true, so we print to screen that "a and b are equal".
"""


print("------------Loops------------")

"""
Python Loops
Python has two primitive loop commands:

while loops
for loops
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

Example
Print i as long as i is less than 6:
"""

i = 1
while i < 6:
  print(i)
  i += 1