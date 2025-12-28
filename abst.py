'''
**4️⃣ Create an abstract class Bank with method interest_rate().

Create subclasses SBI and HDFC and return different interest rates.
Print interest rate using objects.**

**5️⃣ Create an abstract class Payment with abstract method pay().

Create subclasses UPI, Card, and Cash implementing pay() in their own style.**

**6️⃣ Create an abstract class Employee having abstract method calculate_salary().

Create subclasses FullTimeEmployee and PartTimeEmployee and calculate different salaries.**

**7️⃣ Create an abstract class FileReader with abstract method read().

Implement subclasses PDFReader and CSVReader with different read() messages.**

**8️⃣ Create an abstract class Device with abstract method charge().

Create subclasses Mobile and Laptop that override charge().**

**9️⃣ Create an abstract class Database with abstract method connect().

Create subclasses MySQL and MongoDB implementing connect().**

**🔟 Create an abstract class Report with abstract method generate().

Create subclasses PDFReport and ExcelReport printing different messages.**

**1️⃣2️⃣ Create abstract class Game with play().

Subclasses: Cricket, Football, Chess.
Call play() using a list of objects.**'''

'''
*1️⃣ Create an abstract class Shape with an abstract method area().
Then create subclasses Circle and Rectangle that implement area().
Create objects and print all areas.**
'''
from abc import *
class Shape(ABC):
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        print('Area of circle:-',3.14*self.r*self.r)

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print('Area of rectangle:-',self.l*self.b)

r=Rectangle(3,6)
r.area()

'''

**2️⃣ Create an abstract class Animal with abstract methods eat() and sound().
Create subclasses Dog and Cow and implement both methods.
Call both methods using objects.**
'''
from abc import *
class Animal(ABC):
    @abstractmethod
    def eat():
        pass
    @abstractmethod
    def sound():
        pass

class Dog(Animal):
    def eat():
        print('Dog is eating..')
    def sound():
        print('BOW BOW')

class Cow(Animal):
    def eat():
        print('Cow eating..')
    def sound():
        print('mai mai')
c=Cow
c.eat()
c.sound()

'''
**1️⃣1️⃣ Create abstract class Notification with send().
Implement EmailNotification, SMSNotification, PushNotification.**
'''
class Notification(ABC):
    @abstractmethod
    def send():
        pass
class EmailNotification(Notification):
    def send():
        print('Email notification send')
class SMSNotification(Notification):
    def send():
        print('Sms notification send')
class PushNotification(Notification):
    def send():
        print('push noti')
p=PushNotification
p.send()