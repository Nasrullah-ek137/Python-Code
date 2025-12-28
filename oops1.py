
# 1️⃣ Create a class Car with attributes brand and model, create an object and print details.
class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand
    def car_info(self):
        return f"car model name is {self.model} and brand name is {self.brand}"
    
c=Car('Thar','xuv')
print(c.car_info())

# 2️⃣ Create a class Student with constructor that takes name, age and print student info.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def student_info(self):
        return f"Student name is {self.name} and age is {self.age}"
s=Student('Shanu',21)
print(s.student_info())

# 3️⃣ Create a class Employee with method salary(), call this method using an object.
class Employee:
    def salary():
        return "Hello..."
e=Employee
print(e.salary())

# 4️⃣ Create a class BankAccount with deposit and withdraw methods, update balance.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposite(self,amount):
        self.balance=self.balance+amount
        return f"amount deposite successfully check a balance {self.balance}"
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            return f"withdraw amount successfully check a balance {self.balance}"
b=BankAccount(0.0)
print(b.deposite(2000))
print(b.withdraw(2000))

#5️⃣ Create a class Calculator with methods add, sub, mult, div — call using object.
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    
cc=Calculator(12,20)
print(cc.add(),cc.sub(),cc.mult(),cc.div())

# 6️⃣ Make a class Animal and derived class Dog (inheritance), call Dog method.
class Animal:
    def eat():
        return "eating...."
    def sleep():
        return "sleeping"
class Dog(Animal):
    def bark():
        return "bow bow"
d=Dog
print(d.eat())
print(d.bark())
    
# 7️⃣ Make a class Person with method display, inherit it in class Teacher and override display.
class Person:
    def __init__(self,name,age,hobies):
        self.name=name
        self.age=age
        self.hobbies=hobies
    def display(self):
        return f"Name is {self.name} and age is {self.age} and hobies is {self.hobbies}"
class Teacher(Person):
    def display(self):
        return super().display()
t=Teacher('shanu',21,'cricket')
print(t.display())

# 8️⃣ Create a class Vehicle with attribute speed, and subclass Bike that adds mileage. Print both.
class Vehicle:
    speed=120
    def info():
        return f"speed of vehicle is {Vehicle.speed}"
    
    class Bike:
        milege='70kwh'
        def bikeinfo():
            return f"mileage of bike is {Vehicle.Bike.milege}"
        
v=Vehicle
print(v.info())
print(v.Bike.bikeinfo())

# 9️⃣ Create a class Laptop with price & brand, and subclass GamingLaptop that adds RAM and GPU.
class Laptop:
    def __init__(self,price,brand):
        self.price=price
        self.brand=brand
    def laptopinfo(self):
        return f"the price of this laptop is {self.price} and brand is {self.brand}"
    
    class GamingLaptop:
        def __init__(self,ram,gpu):
            super().__init__()
            self.ram=ram
            self.gpu=gpu
        def gaminglaptopinfo(self):
            return f"the ram is {self.ram} and gpu is {self.gpu}"
l=Laptop(10000,'hello')
print(l.laptopinfo())
g=Laptop.GamingLaptop('4GB','4XR')
print(g.gaminglaptopinfo())

'''
✅ 1️⃣ Single Inheritance — Questions
Q4. Create a class Employee with salary attribute. Create Developer class that adds programming_language attribute. Print all details.
'''
class Employees:
    def __init__(self,salary):
        self.salary=salary
    def salarydisp(self):
        return f"salary is {self.salary}"
    
class Developer(Employees):
    def __init__(self,salary,pl):
        super().__init__(salary)
        self.pl=pl

    def displayed(self):
        return f"employee salary is {self.salary} and pl is {self.pl}"
dd=Developer(2345,'python')
print(dd.displayed())
    

# 7. Create classes A & B each with a method show(). Create class C(A, B) and print which show() executes.
class AA:
    def show(self):
        return "show1aa"
    
class BB:
    def show(self):
        return "show2bb"
class C(AA,BB):
    pass
ccx=C()
print(ccx.show())

'''

**Q8. Make two parent classes:

Class Bank → method: bank_info

Class Customer → method: cust_info
Create Account class that inherits both and prints combined details.**'''
class BANK:
    def bank_infoo(self):
        return " This is the detail of bankkk"
class CUSTOMER:
    def cust_infoo(self):
        return "This is the customer infooo"
class ACCOUNT(BANK,CUSTOMER):
    def resultt(self):
        return f"this is the result of bank is {self.bank_infoo()} and this is detail of customer {self.cust_infoo()}"
sa=ACCOUNT()
print(sa.resultt())

'''
**Q10. Create class A with method a1().
Then B(A) with method b1().
Then C(B) with method c1().
Call all methods using C object.**'''
class AAA:
    def A1(self):
        return "a111111"
class BBB(AAA):
    def B1(self):
        return "b111111111"
class CCC(BBB):
    def C1(self):
        return "c111111111111"
xz=CCC()
print(xz.A1())
print(xz.B1())
print(xz.C1())

'''
**Q11. Build a Student hierarchy:

Person → Student → CollegeStudent → FinalYearStudent
Print all inherited attributes.**
'''
class PERSON:
    def per(self):
        return "person info.."
class STUDENTS(PERSON):
    def stuu(self):
        return "student info.."
class COLLEGESTUD(STUDENTS):
    def clgstu(self):
        return "clgstudent info.."
class Finalyearstudents(COLLEGESTUD):
    def fys(self):
        return "final year info..."
fyss=Finalyearstudents()
print(fyss.per())
print(fyss.stuu())
print(fyss.clgstu())
print(fyss.fys())

# Q12. Create class Vehicle → Car → ElectricCar. Add attributes in each class and print all using ElectricCar object.'''
class vehi:
    def __init__(self,engine,wheel):
        self.engine=engine
        self.wheel=wheel
    def vehinfo(self):
        return f"This is vehicle and engine is {self.engine} and wheel is {self.wheel}"
class carss(vehi):
    def __init__(self,engine,wheel,model):
        super().__init__(engine,wheel)
        self.model=model
    def carinfo(self):
        return f"This is car and engine is {self.engine} and wheel is {self.wheel} and car model is {self.model}"
class Electriccar(carss):
    def __init__(self,engine,wheel,model,battery):
        super().__init__(engine,wheel,model)
        self.battery=battery
    def electriccarsinfo(self):
        return f"This is car and engine is {self.engine} and wheel is {self.wheel} and car model is {self.model} and battery is {self.battery}"
    
ew=Electriccar('engine2x',4,'suvv','200khwh')
print(ew.vehinfo())
print(ew.carinfo())
print(ew.electriccarsinfo())

'''

🔥 BONUS (Most Asked in Interviews)
Q21. Write an example of Hybrid Inheritance in real life using classes.
Q22. Check MRO (Method Resolution Order) of a hybrid inheritance class using class C(A, B): pass.
Q23. Show the “diamond problem” using inheritance and solve it using super().'''

'''
Q13. Create base class Shape.

Subclasses: Circle, triangle, Rectangle.
Each calculates its own area.**
'''
class SHAPE:
    def shapeinfo(self):
        return f"This is shape information.."
class CIRCLE(SHAPE):
    def __init__(self,r):
            self.r=r

    def circleinfo(self):
        return f"Area of circle is {3.14*self.r*self.r}"
class TRIANGLE(SHAPE):
    def __init__(self,l,b,h):
        self.h=h
        self.l=l
        self.b=b

    def triangleinfo(self):
        return f"Area of triangle is {self.l*self.b*self.h}"
    
class RECTANGLE(SHAPE):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def rectangleinfo(self):
        return f"Area of ractangle is {self.l*self.b}"
    
ss=SHAPE()
print(ss.shapeinfo())
asd=CIRCLE(10)
print(asd.circleinfo())
sed=TRIANGLE(32,12,43)
print(sed.triangleinfo())
rwq=RECTANGLE(12,43)
print(rwq.rectangleinfo())

'''
**Q14. Create class Animal.

Subclasses: Dog, Cat, Cow.
Each prints its own sound.**
'''
class ANIMALS:
    def anim(self):
        print('this is animal class')
class DOG(ANIMALS):
    def dogsound(self):
        print("BOW BOW")
class CAT(ANIMALS):
    def catsound(self):
        print('meow meow')
class COW(ANIMALS):
    def cowsound(self):
        print('bwue bwue')
asq=ANIMALS()
asq.anim()
df=DOG()
df.dogsound()
md=CAT()
md.catsound()
mq=COW()
mq.cowsound()

'''
Q15. Create class Employee.

Subclasses: Manager, Developer, Designer.
Each prints job role.**'''
class EMPLOYEES:
    def empinfo(self):
        print('Employee information..')

class MANAGER(EMPLOYEES):
    def managerinfo(self):
        print('Manager information..')

class DEVELOPER(EMPLOYEES):
    def developerinfo(self):
        print('developer information')

class DESIGNER(EMPLOYEES):
    def desigerinfo(self):
        print("Designer information..")

mz=EMPLOYEES()
mz.empinfo()
mq=MANAGER()
mq.managerinfo()
bv=DEVELOPER()
bv.developerinfo()
lk=DESIGNER()
lk.desigerinfo()

'''
**Q16. Create a parent class Account.
Subclasses: SavingsAccount, CurrentAccount — each having different withdraw rules.**
'''
class ACCOUNTS:
    def accountrules(self):
        print('Hello this is account class')

class SAVINGSACCOUNT(ACCOUNTS):
    def savingaccrules(self):
        print('saving account means 0 balance account')

class CURRENTACCOUNT(ACCOUNTS):
    def curraccrules(self):
        print('current account means business man it can open')

mn=SAVINGSACCOUNT()
po=CURRENTACCOUNT()

mn.accountrules()
mn.savingaccrules()
po.curraccrules()

'''
**Q18. Create School → Teacher, School → Student,
Then Classroom inherits from both Teacher and Student.
Create object of Classroom and call all methods.**'''

class SCHOOL:
    def show(self):
        print('this is school class')
class TEACHER(SCHOOL):
    def trshow(self):
        print('this is teacher class')
class STUDENTS(SCHOOL):
    def stushow(self):
        print('this is etudent class')
class CLASSROOM(TEACHER,STUDENTS):
    def clroom(self):
        print('Inherit both tr and stud class')
poi=CLASSROOM()
poi.show()
poi.trshow()
poi.stushow()
poi.clroom()

'''
**Q19. Create class Device
Subclass: Computer
Subclass: Phone
Then create SmartDevice inheriting from both Computer and Phone.**
'''
class device:
    def deviceru(self):
        print('Devices class')
class computerss(device):
    def compinfo(self):
        print("computer class")
class phones(device):
    def phoneinfo(self):
        print('Phone class')
class smartdevice(computerss,phones):
    def smdinfo(self):
        print("INgerit both comp and phone class")
zx=smartdevice()
zx.compinfo()
zx.phoneinfo()
zx.smdinfo()


'''
**Q20. Make a hybrid structure:
Person → Employee,
Person → Student,
Intern inherits from both Employee and Student.**
'''
class PERSONI:
    def personi(self):
        print('person class')
class employer(PERSONI):
    def empindf(self):
        print('employee class')
class studentsd(PERSONI):
    def studentssainfo(self):
        print('STudent info..')
class internn(employer,studentsd):
    def inetrs(self):
        print("inherit both emp and stud..")
poil=internn()
poil.personi()
poil.studentssainfo()
poil.inetrs()


# 21. Write an example of Hybrid Inheritance in real life using classes.
class PERson:
    def perinfo(self):
        print('person class')

class STUdent(PERson):
    def stuinfo(self):
        print('student classs')

class clgW(PERson):
    def clgwinfo(self):
        print('clg class')

class LibraraY(STUdent,clgW):
    def libinfo(self):
        print('Library info...')

lqw=LibraraY()
lqw.perinfo()
lqw.stuinfo()
lqw.clgwinfo()
lqw.libinfo()

# Q22. Check MRO (Method Resolution Order) of a hybrid inheritance class using class C(A, B): pass.
class Aa:
    pass
class Bb(Aa):
    pass
class Cc(Aa):
    pass
class Dd(Cc,Bb):
    pass
poq=Dd
print(Dd.mro())

# Q23. Show the “diamond problem” using inheritance and solve it using super().'''
class aA:
    def m11(self):
        print('aa class')
class bB(aA):
    def m12(self):
        print('bb class')
class cC(aA):
    def m13(self):
        print('cc class')
class dD(bB,cC):
    def m14(self):
        super().m11()
        super().m12()

xzse=dD()
xzse.m14()