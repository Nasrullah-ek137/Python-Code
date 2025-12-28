# 1)write py program that prints the following text exactly as it appears
''' python is fun.
"Quotes" and 'single quotes' can be tricky.'''

print('''python is fun.
"Quotes" and 'single quotes' can be trickly.''')

# 2) for the business create 3 variables to store name,age and city.print sentence that uses variables
name = "Shanu"
age = 21
city = 'Mumbai'
print(f"my name is :-{name} and my age is :-{age} and my city is {city}")

# 3)wapp to input student name and marks 3 subjects.print name and percentage in output
student_name = input('Enter student name :- ')
english = int(input('Enter your english marks :-'))
maths = int(input('Enter your maths marks :-'))
history = int(input('Enter your history marks :-'))

percentage = round((english+maths+history)/300 *100,2)

print('Name of student is ',student_name,'The percentage of this 3 subjects is ',percentage,'%')


# 3)wapp that collect multiple type of data like name,age,height,student_status from user input and store
# them in dictionary,and then print out the collected data
student_deatils = {}

student_deatils['stud_name']  = input('Enter student name :-') 
student_deatils['stud_age']  = int(input('Enter student age :-')) 
student_deatils['stud_height']  = float(input('Enter student height :-')) 
student_deatils['stud_status']  = input('Enter student status :-') 

print(student_deatils)


# 4)wap to find leap year to detemine if a given year is leap year using user input

'''
Note 
leap year occurs once every 4 years
year is a leap year if it is divisble by 4,but not if divisible by 100 unless it also divisble by 400'''
leapp = int(input('Enter a year like 2023 :-'))

if (leapp%4 ==0 and leapp%100!= 0) or leapp%400 ==0:
    print('this is leap year',leapp)
else:
    print('this is not leap year',leapp)

# 5)login authentication using conditional statement.asuume you have predefined username and pwd

'''
write program that prompts the user to enter a uername and pwd and check whether they match.provide appropriate
msg for the following cases:
both username and pwd are correct
username is correct but pwd is incorrect
username is incorrect
'''
username =input('Enter username :-')
password =input('Enter password :-')


if username == 'Shanuu' and password == 'Shanu@1137':
    print('Congrate your username and pwd is correct...')
elif username == 'Shanuu' and password != 'Shanu@1137':
    print('oops your usename is correct but your pwd is incoreect try again..')
else:
    print('username is invalid try again..')


# 6)admission eligiblity a university has the following eligibility criteria for admission:
'''
marks in maths >=65
marks in physics >= 55
marks in chemistry >=50
total marks in all three subject >= 180 or total marks in maths and physics >=140
write program that take marks in 3 subjects as input and print whether the student is eligible for admission
'''
mathss = int(input('Enter maths marks :-'))
physics = int(input('Enter physics marks :-'))
chemistry = int(input('Enter chemistry marks :-'))

if (mathss >=65 and physics >=55 and chemistry >=50 and (mathss+physics+chemistry) >=180) or (mathss+physics) >=140:
    print('Congaulation you are eligible for admission')

else:
    print("Sorry you are not eligible for admission next time..")


# 7) write python proram to build simple calculator
''''
availale opr add,sub,mult,div,avg
'''
num1 = int(input('Enter first number :-'))
num2 = int(input('Enter second number :-'))

operation = input('Enter operation you perform..')

if operation == '+' or operation == 'addition' or operation == 'add':
    print('The sum of 2 numbers is :-',num1+num2)

elif operation == '-' or operation == 'subtraction' or operation == 'sub':
    print('The subtraction of 2 numbers is :-',num1-num2)

elif operation == '*' or operation == 'multiplication' or operation == 'multi':
    print("The multiplication of 2 numbers is :-",num1*num2)

elif operation == '/' or operation == 'division' or operation == 'div':
    print('The division of 2 number is :-',num1/num2)

elif operation == 'average' or operation == 'avg':
    print("The average of 2 numbers is :-",(num1+num2)/2)

else:
    print("invalid operator try again...")


# 8)limit decimal places to 2 digits using .format methods and print result, for variable pi = 3.14158696706
pi = 3.14158696706
print('the pi values is {}'.format(round(pi,2)))


# 9)extract characters from index 2 to 8 with step of 2 :
'''
given mystr='python course' slice character from index 2 to 8 skipping every other character
'''
mystr='python course'
print(mystr[2:8])

'''
10) slice to get only middle character for mystr1 = 'madhavi' use slicing to extract middle character
'''
mystr1 = 'madhavi'
print(mystr[3])


'''
11)remove first 3 and last 3 character given mystr2 = 'regression analysis' remove the first 3 and last 3 char
'''
mystr2 = 'regression analysis'
print(mystr2[3:-3])

'''
12) get substring that start 4 character from end to last character for mystr3 = 'classification' slice
str starting from 4th char from end to last character
'''
mystr3 = 'classification'
print(mystr3[-4:])

'''
13) wapy function to check if a str is palindrome using str mthod
'''
word = 'madam'
def palw(s):
    if s == s[::-1]:
        print('palindrome')
    else:
        print("not palindrome")
palw(word)


# 14) Write a Python program to check whether a number is positive, negative, or zero.
number = int(input('Enter a number :- '))

if number > 0:
    print('This number is +ve')
elif number < 0:
    print('This number is -ve')
elif number == 0:
    print('This number is zero')
else:
    print('plz give proper number try again...')


# 15) Write a Python program to check whether a given number is even or odd.
number1 = int(input('Enter a number :- '))

if number1%2==0:
    print(number1,'is even number')
else:
    print(number1,'This number is odd')


''' 16)Write a Python program to take marks of a student and print the grade based on these conditions:
90 and above → A
80–89 → B
70–79 → C
60–69 → D
below 60 → Fail   '''
marks = int(input('Enter a marks :- '))

if marks >= 90:
    print('A grade')
elif marks >= 80 and marks <= 89:
    print('B grade')
elif marks >= 70 and marks <= 79:
    print('C grade')
elif marks >= 60 and marks <=69:
    print('D grade')
else:
    print('Fail')


# 17)Write a Python program to check whether a person is eligible to vote or not based on age.
agee = int(input('Enter your age :- '))

if agee >= 18:
    print('You are eligible for giving vote')
else:
    print('You are not eligible for giving vote')


# 18)Write a Python program to take a year as input and check whether it is a leap year or not.
yearr = int(input('Enter a year :-'))

if (yearr%4==0 and yearr%100!=0) or yearr%400==0:
    print('This year is leap year')
else:
    print('Sorry this year is not leap year')


#19) Write a Python program to check the largest of three numbers using if–elif–else.
a = int(input('Enter first number :- '))
b = int(input('Enter second number :- '))
c = int(input('Enter third number :- '))


if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")


'''20) Write a Python program to check if a character entered by the user is a vowel or a consonant.
Explanation:
User ek single alphabet input karega (like 'a', 'b', 'e', etc.)
A, E, I, O, U → ye vowels hote hain.
Baaki sab alphabets → consonants hote hain.'''

alpha = input('Enter a vowel alphabet :- ')
v = ['a','e','i','o','u']

if alpha in v:
    print('This alphabet is vowels alphabet')
else:
    print('this is consonant alphabet')


''' 21)Write a Python program to check whether a triangle is equilateral, isosceles, or scalene using
the lengths of its three sides.
Explanation:
User se 3 sides ka input lena hai — a, b, c.
Fir conditions check karni hai:
If all three sides are equal → Equilateral Triangle
If any two sides are equal → Isosceles Triangle
If all three sides are different → Scalene Triangle
'''
side1 = int(input('Enter first number :- '))
side2 = int(input('Enter second number :- '))
side3 = int(input('Enter third number :- '))

if side1 == side2 == side3:
    print('Equilateral Triangle')
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("Isosceles Triangle")
else:
    print('Scalene Triangle')


''' 22)Write a Python program that asks the user for a username and password and checks if both are correct, 
otherwise print appropriate messages using if–elif–else.'''

user_username = input('Enter your Username :- ')
user_password = input('Enter your password :- ')

correct_username = 'Nasrullah'
correct_password = 'Shanu@1137'

if user_username == correct_username and user_password == correct_password:
    print('Congrate your username and pwd are valid')

elif user_username == correct_username and user_password != correct_password:
    print('Sorry your username is valid but your pwd is invalid.')

elif user_username != correct_username and user_password == correct_password:
    print('Sorry your password is valid but your username is invalid.')

else:
    print('Both are invalid try again...')


''' 23) Write a Python program that takes a person’s age and citizenship status. If the age is 18 or above, 
then check if the person is Indian citizen. If both conditions are true, print "Eligible for Voting", otherwise
 print "Not Eligible".
'''
ageee = int(input('Enter your age: '))
citizenship_status = input('Enter your country name: ').lower()

if ageee >= 18 and citizenship_status == 'india':
    print('Eligible for Voting')
else:
    print('Not Eligible')

# 24) Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)


# 25) Print even numbers from 1 to 50.
for e in range(1,51):
    if e%2==0:
        print(e)

# 26) Print odd numbers from 1 to 50.
for o in range(1,51):
    if o%2!=0:
        print(o)

#27) Print table of a number entered by user.
user = int(input('Enter any number :-'))

for i in range(1,11):
    print(user,'X',i,'=',user*i) # 2 x 1 = 2 


# 28) Print the sum of numbers from 1 to 100.
result = 0
for s in range(1,101):
    result = result + s
    print(result)


# 29) Print squares of numbers from 1 to 10.

for a in range(1,11):
    print('Square root of this number is ',a*a)

# 30) Print elements of a list using a for loop.
l = [10,20,40,30,50]

for s in l:
    print(s)