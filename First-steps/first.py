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

print('-------------------------------------')

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

print('-------------------------------')

x = 1
y = 35656222554887711
z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))

# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))

x = 3+5j
y = 5j
z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

print('-------------------------------')

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.update({7, 8})

print(my_set)


print('--------------------------------------')

my_string = "Hello World"
result = my_string[::-1]
print(result)

print('--------------------------------------')


my_tuple = (1, 2, 3)
a, *b, c = my_tuple
print(b)

print('--------------------------------------')

my_dict = {'a': 1, 'b': 2, 'c': 3}
# result = my_dict.get('d', 4)
# print(result)
# print(my_dict)

print('--------------------------------------')

x = [1, 2, 3]
y = [1, 2, 3]
# result = x == y
# print(result)

print('--------------------------------------')

x = 10
y = 5

# result = (x > y) and (x < 20) or (y < 0)
# print(result)

print('--------------------------------------')

# s = "hello"
# result = "".join([char * 2 for char in s])
# print(result)

print('--------------------------------------')

s = "apple orange banana cherry grape"
result = s.split(maxsplit=2)
print(result)


print('--------------------------------------')