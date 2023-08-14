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

"""
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

    Function	Description
    findall	    Returns a list containing all matches
    search	    Returns a Match object if there is a match anywhere in the string
    split	    Returns a list where the string has been split at each match
    sub	        Replaces one or many matches with a string
"""

print("---------------------------------------------------")

"""
Metacharacters
Metacharacters are characters with a special meaning:

Character	    Description	Example	Try it
    []	            A set of characters	"[a-m]"	
    \	            Signals a special sequence (can also be used to escape special characters)	"\d"	
    .	            Any character (except newline character)	"he..o"	
    ^	            Starts with	"^hello"	
    $	            Ends with	"planet$"	
    *	            Zero or more occurrences	"he.*o"	
    +	            One or more occurrences	"he.+o"	
    ?	            Zero or one occurrences	"he.?o"	
    {}	            Exactly the specified number of occurrences	"he.{2}o"	
    |	            Either or	"falls|stays"	
    ()	            Capture and group
"""

print("---------------------------------------------------")

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

print("-----")

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

print("-----")

txt = "heaio planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

print("-----")

# txt = "hello planet"
txt = "nohello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

print("-----")

# txt = "hello planet"
txt = "hello planeto"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

print("-----")

# txt = "hello planet"
# txt = "helailo planet"
# txt = "heo planet"
# txt = "hellfob planet"
txt = "haellfob planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

print("-----")

# txt = "hello planet"
# txt = "hellalko planet"
# txt = "hellalkop planet"
txt = "haellalko planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

print("-----")

# txt = "hello planet"
# txt = "helo planet"
txt = "heo planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

print("-----")

# txt = "hello planet"
txt = "hellllo planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)
x = re.findall("he.{4}o", txt)

print(x)

print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
