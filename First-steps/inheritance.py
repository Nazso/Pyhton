"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:

Example
Create a class named Person, with firstname and lastname properties, and a printname method:
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


print("--------------------------------------------")

"""
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Example
Create a class named Student, which will inherit the properties and methods from the Person class:
"""

class Student(Person):
  pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

# Use the Student class to create an object, and then execute the printname method:

y = Student("Mike", "Olsen")
y.printname()

print("--------------------------------------------")

"""
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""

"""
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

Example
"""

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

z = Student("Luke", "Skywalker")
z.printname()

"""
Now we have successfully added the __init__() function,
and kept the inheritance of the parent class,
and we are ready to add functionality in the __init__() function.
"""

print("--------------------------------------------")

# other example!!!

class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()

print("--------------------------------------------")

class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by 
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
# t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()

print("--------------------------------------------")

"""
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

Example
"""
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

xx = Student("Matt", "LeBlanc")
xx.printname()

# By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.

print("--------------------------------------------")

xy = Student("Peter", "Griffin")
print(xy.graduationyear)

# In the example below, the year 2019 should be a variable,
# and passed into the Student class when creating student objects.
# To do so, add another parameter in the __init__() function:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Meg", "Griffin", 2005)
print(x.printname())
print(x.graduationyear)


print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")
