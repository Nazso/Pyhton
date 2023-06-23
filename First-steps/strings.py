a = "Hello"
print(a)

print('-----------------------')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print('-----------------------')

a = "Hello, World!"
print(a[1])
print(a[8])

print('-----------------------')

for x in "banana":
  print(x)

print('-----------------------')

a = "Hello, World!"
print(len(a))

print('-----------------------')

txt = "The best things in life are free!"
print("free" in txt)
print("best" in txt)
print("stirng" in txt)

print('-----------------------')

txt = "The best things in life are free!"
print("expensive" not in txt)

print('-----------------------')

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

print('-----------------------')

b = "Hello, World!"
print(b[1:5])

print('-----------------------')

b = "Hello, World!"
print(b[:4])

print('-----------------------')

b = "Hello, World!"
print(b[2:])

print('-----------------------')

b = "Hello, World!"
print(b[-10:-2])

print('-----------------------')

aaa = "Practice Python with happy face!"
aab = "      Practice Python with happy face!"
print(aaa.upper())
print(aaa[12:18].upper())
print(aaa.lower())
print(aab.strip())
print(aaa.replace("P", "Q"))
print(aaa.split(" "))
abb = aaa.split(" ")
print(abb)
ff = abb[1]
gg = abb[2].upper().replace("H", "C")
print(ff)
print(gg)

print('-----------------------')

aba = "Hello"
bba = "World"
cca = aba + bba
print(cca)
print(aba + bba + '!')

abba = "Hello"
bab = "World"
caa = abba + " " + bab + "!"
print(caa)

print('-----------------------')

age = 36
#txt = "My name is John, I am " + age #Ez így nem működhet!!!
# print(txt)

#A helyes megoldás: format() metódus alkalmazása!!!
age = 36
old = 127
txt = "My name is John, and I am {} years old"

name = "Jakab"
txta = "My name is {}, and I am {} years old"

born = 1526
name = "Jakab"
txtb = "My name is {0}, I was born in {2} and I am {1} years old. And I am terrible in Math..."

print(txt.format(age))
print(txta.format(name, old))
print(txta.format(old, name))
print(txtb.format(name, old, born))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print('-----------------------')

txtc = "We are the so-called \"Vikings\" from the north."
print(txtc)

txtd = "We are\nthe so-called \"Vikings\" from the north."
txte = "We are \rfrom the north."
txtf = "We are\tthe so-called \"Vikings\" from the north."
txtg = "We are\bthe so-called \"Vikings\" from the north."
txth = "We are\fthe so-called \"Vikings\" from the north."
txti = "\113\125\164\157\159" #\ooo, octal value
txtj = "\x48\x65\x6c\x6c\x6f" #\xhh, Hex value

print(txtd)
print(txte)
print(txtf)
print(txtg)
print(txth)
print(txti)
print(txtj)

print('-----------------------')

alpha = "alpha"
alphaOne = "/=alpha23"
beta = "My name is Ståle"

print(txtb.format(name, old, born).capitalize())
print(txtb.format(name, old, born).casefold())

print(alpha.center(30))
print(alpha.center(30, "T"))

print(txtb.format(name, old, born).count('in'))
print(txtb.format(name, old, born).count('in', 15, 35))

print(beta.encode())
print(beta.encode(encoding="ascii",errors="backslashreplace"))
print(beta.encode(encoding="ascii",errors="ignore"))
print(beta.encode(encoding="ascii",errors="namereplace"))
print(beta.encode(encoding="ascii",errors="replace"))
print(beta.encode(encoding="ascii",errors="xmlcharrefreplace"))

print(txtb.format(name, old, born).endswith('.'))
print(txtb.format(name, old, born).endswith('g'))
print(txtb.format(name, old, born).endswith('g', 2, 10))
print(txtb.format(name, old, born).endswith('e', 2, 7))

print(txtb.format(name, old, born).rfind('in'))
print(txtb.format(name, old, born).rindex('am'))


print(alpha.isalnum())
print(alphaOne.isalnum())
print(alpha.isalpha())
print(alphaOne.isalpha())

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

print('-----------------------')

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

print('-----------------------')

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want {:.2f} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print('-----------------------')

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print('-----------------------')

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
