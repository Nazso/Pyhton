"""
Python File Open

File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.


There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

The code above is the same as:

Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.
"""
# f = open("demofile.txt")
# f = open("demofile.txt", "rt")


"""
Open a File on the Server
Assume we have the following file, located in the same folder as Python:

To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
"""

f = open("demofile.txt", "r")
print(f.read())

print("--------------------------Read Only Parts of the File---------------------------------")

"""
If the file is located in a different location, you will have to specify the file path, like this:

Example
Open a file on a different location:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
"""

"""
Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:

Example
Return the 5 first characters of the file:
"""

# f = open("demofile.txt", "r")
f = open("demofile.txt")
# What is the deifference with or without "r"????

print(f.read(5))
print(f.read(13))
print(f.read(30))

print("----------------------------Read Lines-------------------------------")

"""
Read Lines
You can return one line by using the readline() method:

Example
Read one line of the file:
"""


f = open("demofile.txt", "r")
print(f.readline())

print("-----------------")

"""
By calling readline() two times, you can read the two first lines:

Example
Read two lines of the file:
"""

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print("-----------------")

"""
By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:
"""

f = open("demofile.txt", "r")
for x in f:
  print(x)


print("----------------------------Closee files-------------------------------")

"""
Close Files
It is a good practice to always close the file when you are done with it.

Example
Close the file when you are finish with it:
"""

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Note: You should always close your files, in some cases, due to buffering,
# changes made to a file may not show until you close the file.

print("-----------------------------wirte file-------------------------")

"""
Python File Write
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

Example
Open the file "demofile2.txt" and append content to the file:
"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

print("------------------")

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

"""
Example
Open the file "demofile3.txt" and overwrite the content:

"""

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

print("------------------")

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

print("------------------")
