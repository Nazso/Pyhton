print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(11 % 5)
print(10 ** 5)
print(19 // 5)

print('----------------------------')

x = 5
x += 3

print(x)


x = 5
x -= 3

print(x)


x = 5
x *= 3

print(x)


x = 5
x /= 3

print(x)


x = 5
x %= 3

print(x)


x = 5
x //= 3

print(x)


x = 5
x **= 3

print(x)
x = 5
x &= 3

print(x)


x = 5
x |= 3

print(x)


x = 5
x ^= 3

print(x)



#The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

#If you push 00 in from the left:
# 3 = 0000000000000011
#becomes
#12 = 0000000000001100

x = 5
x <<= 3

print(x)

y = 3
y <<= 2

print(y)


x = 5
x >>= 3

print(x)


print('----------------------------')

x = ["apple", "banana"]

print("banana" in x)
print("melone" in x)

print("pineapple" not in x)
print("apple" not in x)

# returns True because a sequence with the value "banana" is in the list

print('----------------------------')

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # returns True because z is the same object as x

print(x is y)   # returns False because x is not the same object as y, even if they have the same content

print(x == y)   # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print('----------------------------')

x = 5

print(x > 3 and x < 10)     # returns True because 5 is greater than 3 AND 5 is less than 10

print(x > 3 or x < 4)       # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

print(not(x > 3 and x < 10))    # returns False because not is used to reverse the result

print('----------------------------')

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print('----------------------------')

print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(6 | 3)

"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
"""

print(6 ^ 3)

"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
"""

print(~3)
print(~7)

"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
"""


print('----------------------------')

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)
