
# 1️⃣ Write a function to print “Hello World” (no parameters, no return).
def demoo():
    print('Hello world')

demoo()

# 2️⃣ Write a function that takes a name as parameter and prints a greeting.
def naam(name):
    print(f"My name is {name}")
naam('Shanuu')

# 3️⃣ Write a function that takes two numbers and returns their sum.
def summ(a,b):
    print("The sum of 2 number is ",a+b)

summ(10,32)

# 4️⃣ Write a function that checks whether a number is even or odd.
def checkk(num):
    if num%2==0:
        print('this number is even')
    else:
        print("this number is odd..")

checkk(857)

# 5️⃣ Write a function that takes a list and returns the count of even numbers.'''
l = [10,34,22,34,65,47,98,87]

def cc():
    cou=0
    for i in l:
        if i%2==0:
            cou = cou+1
    print(cou)
cc()


# 6️⃣ Write a function to calculate SI: simple_interest(p, r=5, t=1).  SI = (P × R × T) / 100
def si(p,r=5,t=1):
    return p*r*t/100

sii=si(p=10)
print(sii)

# 7️⃣ Write a function to greet a user with default name = “Guest”.
def gree(namee='Guest'):
    print(f"Hello user what your name {namee}")

gree()

# 8️⃣ Write a function to calculate power of a number, default exponent=2
def po(num,exponent = 2):
    return num**exponent

power=po(23)
print(power)

# 9️⃣ Write a function student_info(name, age, city) and call it using keyword arguments.
def student_info(name,age,city):
    print(f"Student name is {name} and student age is {age} and city is {city}")

student_info(city='Mumbai',age=21,name='Shanu')

# Write a function that formats a sentence like: introduce(name="Shanu", skill="Python", city="Mumbai")
def introduce(name="Shanu", skill="Python", city="Mumbai"):
    print(f"my name is {name} and i am learning skill of {skill} and my city is {city}")

introduce()

# *1️⃣1️⃣ Write a function that accepts args and returns the sum of all numbers.
def all_nu(*args):
    sum=0
    for num in args:
        sum=sum+num
    print(sum)

all_nu(1,6,54,32,87,55)

# *1️⃣2️⃣ Write a function that accepts args and returns the largest element.
def large(*args):
    l1 = []
    for s in args:
        if s==max(args):
            print(max(s))
        return s
    
w=large([32,65,87,22,34])
print(w)

# *1️⃣3️⃣ Write a function that prints all values passed through args on new lines.
def new(*args):
    for v in args:
        print(v)

new(120,34,2321,23,4,23,22)

# **1️⃣4️⃣ Write a function that accepts kwargs and prints key-value pairs.
def fn(**kwargs):
    for x,y in kwargs.items():
        print(f"{x} is {y} ",end='')

fn(name='shanu',age=21,city='mumbai')

# **1️⃣5️⃣ Write a function employee_info(kwargs) that prints details like name, id, salary.
def employee_info(**kwargs):
    for x,y in kwargs.items():
        print(f"Employee {x} is :- {y}")

employee_info(name='shanu',id=101,salary=20394)

# **1️⃣6️⃣ Write a function that uses both *args and kwargs in the same function.
def both(*args, **kwargs):
    pass

# 1️⃣7️⃣ Write a function to reverse a string using a for loop (no slicing).
def rev(strr):
    r=''
    for m in range(len(strr),0,-1):
        print(m)
rev('shanuuu')

'''
1️⃣ Write a function to print the square of numbers from 1 to 10.
2️⃣ Write a function to print factorial of 5.
3️⃣ Write a function to print even numbers from 1 to 50.
4️⃣ Write a function to display all vowels in a string (string inside function only).
5️⃣ Write a function to print Fibonacci series up to 10 terms.'''

# 1️⃣ Write a function to print the square of numbers from 1 to 10.
def square():
    for i in range(1,11):
        print(i**2)
square()

# 2️⃣ Write a function to print factorial of 5.
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

r = fact(5)
print(r)

# 3️⃣ Write a function to print even numbers from 1 to 50.
def even():
    for i in range(1,51):
        if i%2==0:
            print(i)

even()

# 4️⃣ Write a function to display all vowels in a string (string inside function only).
def vow(strr):
    l=['a','e','i','o','u']
    s=''
    for ch in strr:
        if ch in l:
            s=s+ch
    print(s)
vow('shanuuuwe')

'''
🔥 reduce() — 3 Questions

(Needs from functools import reduce)

1️⃣5️⃣ Use reduce() to find the sum of all numbers in a list.
1️⃣6️⃣ Use reduce() to find the product of all numbers in a list.
1️⃣7️⃣ Use reduce() to find the maximum value in a list.

🔥 Combined — map(), filter(), reduce(), lambda — 3 Questions

1️⃣8️⃣ Use map + filter to square only even numbers.
1️⃣9️⃣ Use filter + reduce to get sum of odd numbers.
2️⃣0️⃣ Use map + reduce to get sum of squares of numbers.'''

# 1️⃣ Write a lambda to add two numbers.
add = lambda x,y:x+y
print(add(2,3))

# 2️⃣ Write a lambda to find square of a number.
squaree=lambda x:x**2
print(squaree(5))

# 3️⃣ Write a lambda to check if a number is even.
ev=lambda x:x%2==0
print(ev(6))

# 4️⃣ Write a lambda to return last character of a string.
st=lambda x:x[-1]
print(st('shanu'))


# 7️⃣ Use map() to square each element in a list.
l=[1,5,8,7,2]
squ=list(map(lambda x:x**2,l))
print(squ)

# 8️⃣ Use map() to convert all strings in a list to uppercase.
s='shanuuausussu'
st=list(map(lambda x:x.upper(),s))
print(st)

# 9️⃣ Use map() to check even/odd for each number in a list.
l1=[2,5,3,23,87,54,3,4,56]
es=list(map(lambda x:'even' if x%2==0 else 'odd',l1))
print(es)

# 🔟 Use map() with lambda to multiply each list element by 10.
l2=[23,21,39,43,23,11]
mu=list(map(lambda x:x*10,l2))
print(mu)

# 1️⃣1️⃣ Use filter() to get only even numbers from a list.
l3=[12,3,43,4,32,45,6,7,7,6,67,6,654]
evem=list(filter(lambda x: x%2==0,l3))
print(evem)

# 1️⃣2️⃣ Use filter() to get only numbers greater than 50.
l4=[293,34,23,122,50,45,5,54,51]
gr=list(filter(lambda x: x> 50,l4))
print(gr)

# 1️⃣3️⃣ Use filter() to get only vowels from a string.
'''vowels=['a','e','i','o','u']
ste='Shanuuuuudusddjekkfj'
fi=list(filter(lambda x:vowels in x,ste))
print(fi)'''

# 1️⃣4️⃣ Use filter() to get names that start with “A”.
'''sr=list(filter(lambda x: x[0]=='a' in x))
print(sr(['shanu','hello','sonu']))'''

