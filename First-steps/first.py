# print('Hello world!')

# if 5 > 2:
    # print("Five is greater than two!")

#This is just a test of comment

# """
# Multiline comment
# """

# x = 5
# y = 'Try to learn Python'

# print(x, y)
# print(type(x))

# x = "Öt"
# print(x)
# print(type(x))

# a = str(4)
# b = int(4)
# c = float(4)

# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))

# aa, bb, cc = "elephant", "banana", "joke"

# print(aa)
# print(bb)
# print(cc)


# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# xx = "Python "
# yy = "is "
# zz = "awesome"
# print(xx + yy + zz)

# xy = 5
# yx = 10
# print(xy + yx)

# aaa = "more awesome"

# def myfunc():
#   print("Python is " + aaa + "!")

# myfunc()

# xo = "awesome"

# def myfunc():
#   xo = "fantastic"
#   print("Python is " + xo)

# myfunc()

# print("Python is " + xo)

x = 'no OK'

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = str("Hello World")
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))
