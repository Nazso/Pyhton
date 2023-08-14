"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

"""
import re

# txt = "The rain in Spain"
txt = "alfa, beta gamma"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
