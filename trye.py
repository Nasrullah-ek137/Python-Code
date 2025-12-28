'''num1=int(input("Enter a number1 :-"))
num2=int(input('Enter a number2 :-'))
try:
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print('plz give another number not zero')

print('Done !')

try:
    div=num1/num2
    print(di)
except ZeroDivisionError:
    print('Plz provide another number..')
except NameError:
    print('Plz check your variable name is proper or not')
except ValueError:
    print('plz provide proper value')

print('done..')

try:
    div=num1/num2
    print(div)
except (ZeroDivisionError,NameError):
    print('Something was missing')

print('finally')

try:
    div=num1/num2
    print(di)
except (ZeroDivisionError,NameError) as error:
    print(error)
print('finally')

try:
    div=num1/num2
    print(di)
except:
    print("Something is missing")
print('done')

try:
    f=open('shanu.txt','r')
    data=f.read()
    print(data)
except FileNotFoundError as error:
    print(error)
else:
    print('If no error occur then else block will be excuted')

try:
    div=num1/num2
    print(div)
except Exception as error:
    print(error)
    print(error.__class__)
print('Done..')

try:
    age=int(input('enter your age:-'))
    if age < 0:
        raise ValueError('Invalid age try again.')
    print('hello age',age)
except ValueError as var:
    print(var)

class fivedivisionerror(Exception):
    def __init__(self):
        print('FiveDivisonError')
    pass
try:
    num1=int(input("Enter a number1 :-"))
    num2=int(input('Enter a number2 :-'))
    if num2==5:
        raise fivedivisionerror
    div=num1/num2
    print(div)
except (fivedivisionerror,ZeroDivisionError) as error:
    print(error)
print('done.')

def get_square():
    try:
        num=int(input('Enter a number:-'))
        print(num**2)
    except Exception as error:
        print(error)
        get_square()
get_square()

def get_list(my_list):
    total=0
    for i in my_list:
        try:
            int(i)
        except:
            print(f"item {i} is not found")
        else:
            total=total+i
    return total
print(get_list([1,'a','b',3]))'''

def validd(age):
    assert (age >= 0,'age cannot be -ve')
    print(age)

validd(10)
validd(-2)
