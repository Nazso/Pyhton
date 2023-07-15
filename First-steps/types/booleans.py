print(10 > 9)
print(10 == 9)
print(10 < 9)

print('-------------------------')

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print('-------------------------')

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

xx = ""
yy = 0

print(bool(xx))
print(bool(yy))

print(bool(["apple", "cherry", "banana"]))
print(bool([]))

print(bool(False))
print(bool(None))
print(bool(()))
print(bool({}))


print('-------------------------')

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print('-------------------------')

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print('-------------------------')

xxx = 200
yyy = "200"
print(isinstance(xxx, int))
print(isinstance(yyy, int))

print('-------------------------')
print('-------------------------')