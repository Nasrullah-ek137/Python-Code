

'''
**1️⃣ Create a class Student with private attributes name and marks.
Provide setter and getter methods to update and fetch values.**
'''
class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.__name=name
        self.__marks=marks

    def getname(self):
        return self.__name

    def getmarks(self):
        return self.__marks
    
s=Student(101,'shanuu',103)
print(s.getmarks())
print(s.getname())

'''
*2️⃣ Create a class BankAccount with private balance.

Allow deposit and withdraw only through methods, direct access should not be allowed.**
👉 Test:
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.__balance)   ❌ (should give error)
'''
class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposite(self,amount):
        self.__balance+=amount
        print(f'Your deposite amount is {amount} and balance is {self.__balance}')
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print('Insufficient balance')
        else:
            self.__balance-=amount
            print(f'your withdraw is successdul')
    def getbalance(self):
        return self.__balance
ba=BankAccount(100)
ba.deposite(1000)
ba.withdraw(500)
print(ba.getbalance())

'''
**3️⃣ Create a class Employee with private salary attribute.
Add a method to give bonus and update salary.
Salary must not be directly accessible.**
'''
class Employee:
    def __init__(self,ename,salaryy):
        self.ename=ename
        self.__salaryy=salaryy
    def bonusfn(self,bonuss):
        print(f'The current salary is {self.__salaryy} after bonus this salary is {bonuss+self.__salaryy}')
    def getsalary(self):
        return self.__salaryy
em=Employee('shanuu',123450)
em.bonusfn(2340)
#print(em.__salaryy)
print(em.getsalary())

'''
4️⃣ Create a class Car with private attribute __speed.
Write methods to increase_speed() and decrease_speed() but prevent setting negative speed.**
'''
class Carr:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.__speed=speed
    def increase_speed(self,speedd):
        print(f'Your current speed is {self.__speed} you increse your speed {self.__speed+speedd}')
    def decrese_speed(self,speedd):
        print(f'Your current speed is {self.__speed} you decrease your speed {self.__speed-speedd}')
ca=Carr('MArutii','THAR',100)
ca.increase_speed(20)
ca.decrese_speed(50)


'''
**5️⃣ Create a class Laptop with private attributes price and brand.
Allow user to update price only through a method validate_price().**
'''
class Laptop:
    def __init__(self,laptopname,pricee,brandd):
        self.laptopname=laptopname
        self.__pricee=pricee
        self.__brandd=brandd
    def display(self):
        print(f"Laptop name is {self.laptopname} and current price is {self.__pricee} and laptop brand is {self.__brandd}")
    def validate_price(self,updprice):
        print(f'The current price of this laptop is {self.__pricee} but user must say update the price then updated price is {self.__pricee-updprice}')

la=Laptop('DELL',54000,'latitude')
la.display()
la.validate_price(4000)

'''
*6️⃣ Create a class Person with private attribute __age.
Only allow updating age if new value ≥ 0, otherwise show error.**
'''
class Personn:
    def __init__(self,pname,age):
        self.pname=pname
        self.__age=age
    def disp(self):
        print(f"Name of a person is {self.pname} and age is {self.__age}")
    def updagee(self,upage):
        if upage >=0:
            print(f'Your updated age is {self.__age+upage}')
        else:
            print('ERorrr')
pe=Personn('employees',21)
pe.disp()
pe.updagee(4)

'''
**Create a class User with private password.
Provide methods: set_password(), check_password(), and change_password().
Ensure password is never printed.**

Example:
u = User("Nasrullah", "abc123")
u.check_password("abc123") → correct
u.change_password("abc123", "xyz999")
'''
class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def set_password(self):
        self.__password = 'abc123'

    def check_password(self,check_pwd):
        if check_pwd=='abc123':
            print('Password is successfully')
        else:
            print('pwd is incorrect')
    def change_password(self,oldpwd,currepwd):
        if oldpwd=='abc123':
            print('plz enter new pwd')
        if currepwd=='xyz999':
            print('Your pwd is updated...')
u=User('Nasrullah','abc123')
u.check_password('abc123')
u.change_password('abc123','xyz999')
    
        