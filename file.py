'''f=open('practice.txt','r')
c=f.read(10)
#c=f.readline()
#c=f.readlines()
print(c)

with open('practice.txt','r') as f:
    data=f.read()
    data=f.readline()
    data=f.readlines()
    print(data)

with open('practice.txt','w+') as f:
    f.write('Hello shanu bhai kaise hooo')
    f.seek(3)
    print(f.read())

with open('practice.txt','a') as a:
    a.write('meowwwww')

f1=open('me.jpg','rb')
f2=open('palestine.jpg','wb')
ff=f1.read()
f2.write(ff)

with open('practice.txt','r') as f:
    f1=f.read()
    if 'shanu' in f1:
        print('yes')
    else:
        print('no')

with open('shannn.txt','w') as w:
    w.write('name is shanu')
    w.write('class is graduation')

with open('shannn.txt','r') as f:
    ls=f.readlines()
    print(len(ls))

with open('shannn.txt','r') as f:
    data = f.read()
    ls=data.split(' ')
    print(ls)

with open("shannn.txt",'r') as f:
    data=f.read()
    a,d,s,sc=0,0,0,0
    for character in data:
        if character.isalpha():
            a += 1
        elif character.isdecimal():
            d += 1
        elif character.isspace():
            s += 1
        else:
            sc += 1
print('alphabet is :',a)
print('digit is ',d)
print('space is ',s)
print('special character is',sc)

with open('shannn.txt','r') as f:
    data=f.readlines()
    for i in data:
        a,d,s,sc=0,0,0,0
        for character in i:
            if character.isalpha():
                a += 1
            elif character.isdigit():
                d += 1
            elif character.isspace():
                s += 1
            else:
                sc += 1
        print("Alphabets is :",a)
        print('Digits ',d)
        print('space is',s)
        print('special character',sc)

f=open('shannn.txt','r')
data=f.read()
v,c=0,0
va=['a','e','i','o','u','A','E','I','O','U']

for ch in data:
    if ch in va:
        v += 1
    elif ch.isalpha():
        c += 1
    
print('Vowels',v)
print('consonant',c)

with open('shannn.txt','r') as f:
    data=f.readlines()

    for i in data:
        v,c=0,0
        va=['a','e','i','o','u','A','E','I','O','U']
        for character in i:
            if character in va:
                v += 1
            elif character.isalpha():
                c += 1
        
        print(i)
        print('vowels',v)
        print('conconant',c)

with open('shannn.txt','r') as f:
    data = f.read()
    ls=data.split(' ')
    vc=0

    for i in ls:
        for char in i:
            if char in ['a','e','i','o','u','A','E','I','O','U']:
                vc += 1
                break
print(vc)

f1=open('shannn.txt','r')
f2=open('shanu.txt','w')
data=f1.read()
f2.write(data)

f1.close()
f2.close()

f1=open('shannn.txt','r')
f2=open('shanu.txt','w')

data=f1.read()
ls=data.split(' ')

f2.write(str(len(ls)))
f1.close()
f2.close()

f1=open('shannn.txt','r')
f2=open('shanu.txt','w')
ls=f1.readlines()
for i in ls:
    f2.write(i.title())
    print(i.title())

f1.close()
f2.close()


f1=open('shannn.txt','r')
f2=open('shanu.txt','w')

data=f1.read()
ls=data.split(' ')

for i in ls:
    f2.write(i+'\n')
f1.close()
f2.close()


f1=open('shannn.txt','r')
f2=open('shanu.txt','w')
data=f1.readlines()
i=1

for ch in data:
    f2.write(str(i)+' '+ch)
    i=i+1
f1.close()
f2.close()

f1=open('shannn.txt','r')
f2=open('shanu.txt','w')
data=f1.read()

f2.write(data.upper())
f1.close()
f2.close()

f1=open('shannn.txt','r')
f2=open('shanu.txt','w')
data=f1.read()

for ch in data:
    if ch.isalpha():
        f2.write('*')
    elif ch.isdigit():
        f2.write('#')
    elif ch.isspace():
        f2.write('-')
    else:
        f2.write(ch)
f1.close()
f2.close()

import csv
f=open('shanu.csv','r')
data=csv.reader(f,delimiter=',')
i=list(data)
print(i)
f.close()

import csv
f=open('shanu.csv','r')
data=csv.reader(f,delimiter=',')
i=list(data)
for ch in i:
    print(ch)
f.close()

import csv
f=open('hello.csv','w')

data=csv.writer(f,delimiter=',')
data.writerow([10,20,30,40,50])
data.writerow([20,40,60,80,100])
data.writerow([30,60,90,120,150])

f.close()

import csv
f=open('hello.csv','a')

a=csv.writer(f,delimiter=',')

data=[
    [10,20,30,40,50],
    [20,40,60,80,100],
    [30,60,90,120,150],
    [40,80,120,160,200]]
a.writerows(data)
f.close()

import csv
f=open('shanu.csv','w')
data=csv.writer(f,delimiter=',')

st=[]
no=int(input('enter no of stud'))
for i in range(no):
    rn=int(input('enter roll no'))
    name=input('name of student')
    age=int(input('age of student'))
    classs=input('enter class')

    st.append([rn,name,age,classs])

data.writerow(st)
f.close()'''

f=open('shannn.txt','r')
print(f.tell())

print(f.seek(5))
