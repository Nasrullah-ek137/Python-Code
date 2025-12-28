# wap program to store your name,age,and height in variables and print their type  variable and datatype
# wap program to input 2 number and print their sum,difference,product,quotient   arith opr
# create list of 5 fruits add one more fruits.and remove one existing fruit  list append remove
#create tuple of 4 numbers and print first and last element tupe,access element

#create a dict with keys name,age and city change the city and print upd dictionary  dict,access and upd

# create list of number sort it reverse it list method sort,reverse

# check if a num is positive and even using logical opr comparison and logical opr

#carete dict and create key,value and key,value pair


# 1 wap program to store your name,age,and height in variables and print their type  variable and datatype
name = 'shanu'
print(name)
print(type(name))

age = 21
print(age)
print(type(age))


height = 5.4
print(height)
print(type(height))


# 2 create list of 5 fruits add one more fruits.and remove one existing fruit  list append remove
l = ['apple','mango','banana','orange','pineapple']
print(l)

l.append('mango')
print(l)

l.remove('orange')
print(l)

# 3 create tuple of 4 numbers and print first and last element tupe,access element
t = (10,20,30,40)
print(t)

t1 = t[0]
t2 = t[3]
print(t1,t2)

# or

print(t[0],t[3])

# 4 create a dict with keys name,age and city change the city and print upd dictionary  dict,access and upd
d = {
'name':'shanuu',
'age': 21,
'city':'mumbai'
}

d1 = d['city'] = 'Bangluru'
print(d1)

print(d)

# 5 create list of number sort it reverse it list method sort,reverse
l = [10,30,40,20,50]

l.sort()
print(l)

l.reverse()
print(l)
 # or
l.sort(reverse=True)
print(l)

# 6 wap program to input 2 number and print their sum,difference,product,quotient   arith opr
a=int(input('enter a number1:-'))
b=int(input('enter number2:-'))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 7 check if a num is positive and even using logical opr comparison and logical opr
num = int(input('enter a number:-'))
demo = num > 0 and num%2==0
print(demo)

# 8 carete dict and create key,value and key,value pair
d = {'a':10,'b':20,'c':30}
print(d)

print(d.keys())
print(d.values())
print(d.items())