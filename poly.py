
'''
1️⃣ Write a Python program to demonstrate method overriding using two classes Animal and Dog.
(Parent: sound(), Child: sound())
'''
class Animal:
    def sound(self):
        print('Voice of animals')
class Dog(Animal):
    def sound(self):
        print('BOW BOW')
dd=Dog()
dd.sound()

'''Create two classes Circle and Square. Both should have an area() method. Write code to call area() for both
 objects using polymorphism.**'''
class Circle:
    r=10
    def Area(self):
        print('Area of circle is',3.14*Circle.r*2)
class Square:
    l=10
    b=20
    def Area(self):
        print('Area of square is ',Square.l*Square.b)
cc=Circle()
ss=Square()
cc.Area()
ss.Area()

'''
Write a function that takes any object having a show() method (Duck Typing). Pass 2 different objects with same method name.**
'''
class Duck:
    def show(self):
        print('DUCK DUCK..')
class Horse:
    def show(self):
        print('Tapak Tapak')

d=Duck()
h=Horse()
d.show()
h.show()

'''
4️⃣ Create a class Calculator with method add(a, b).

Create another class ScientificCalculator with the SAME method name add(a, b).
Show polymorphism by calling add() for both classes.**
'''
class Calculator:
    def Add(a,b):
        print(a+b)
class ScientificCalculator:
    def Add(a,b):
        print(a+b)
cal=Calculator
scc=ScientificCalculator
cal.Add(10,49)
scc.Add(12,43)

'''
**5️⃣ Write a program where different classes have a common method start_engine().
Call the same method using polymorphism for Car, Bike, Truck classes.**
'''
class Car:
    def startengine(self):
        print('Start your car engine...')
class Bike:
    def startengine(self):
        print('STart your bike engine..')
class Truck:
    def startengine(self):
        print('Start your big truck engine..')
o=Car()
q=Bike()
u=Truck()
o.startengine()
q.startengine()
u.startengine()

'''
Q1️⃣. Create a class Distance that overloads the + operator to add two distances (in km).

Example:
d1 = Distance(10)
d2 = Distance(20)
print(d1 + d2)  # Output: 30 km'''
class Distance:
    def __init__(self,dist):
        self.dist=dist
    def __add__(self,other):
         return self.dist+other.dist
di=Distance(10)
d2=Distance(20)
print(di+d2)

'''
2️⃣. Create a class Book that overloads the > operator to compare book page counts.
Example:
b1 > b2  # True or False based on number of pages
'''
class Book:
    def __init__(self,page):
        self.page=page
    def __gt__(self,other):
        return self.page > other.page
b1=Book(20)
b2=Book(40)
print(b1 > b2)

'''
Q3️⃣. Create a class Salary that overloads the * operator to multiply salary by months.

Example:
s = Salary(30000)
print(s * 12)'''
class Salary:
    def __init__(self,salary):
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.salary
ss=Salary(20000)
sx=Salary(6)
print(ss*sx)

'''
Q4️⃣. Create a class Student that overloads the == operator to check if two students have same marks.
Example:
s1 == s2  # True if marks equal
'''
class Students:
    def __init__(self,marks):
        self.marks=marks
    def __eq__(self,other):
        return self.marks == other.marks
sa=Students(10000)
sw=Students(10000)
print(sa==sw)

'''
Q5️⃣. Create a class ListAdder that overloads the + operator to merge two lists.
Example:
l1 + l2  # returns one combined list
'''
class ListAdder:
    def __init__(self,*args):
        self.args=args
    def __add__(self,other):
        return self.args+other.args
la1=ListAdder(1,2,3,4,5)
la2=ListAdder(2,4,6,8,10)
print(la1+la2)

'''
1. Create a class Vector and overload the + operator to add two vectors.
Example:
v1 = Vector(2,3)
v2 = Vector(1,5)
v1 + v2 → (3, 8)
'''
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return (self.a + other.a,self.b+other.b)
v1=Vector(2,3)
v2=Vector(1,5)
print(v1+v2)
