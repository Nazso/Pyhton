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

print(txt.format(age))
print(txta.format(name, old))
print(txta.format(old, name))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print('-----------------------')
print('-----------------------')
print('-----------------------')
