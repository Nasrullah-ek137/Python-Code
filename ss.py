'''

1️⃣2️⃣ Print this pattern:
****
****
****
****

1️⃣3️⃣ Print this pattern:
1
12
123
1234
12345

1️⃣4️⃣ Print a 3×3 matrix using numbers 1–9.

Output:

1 2 3
4 5 6
7 8 9

1️⃣5️⃣ Print multiplication tables from 1 to 5 using nested while.
1️⃣6️⃣ Print reverse star triangle:
*****
****
***
**
*

1️⃣7️⃣ Print alphabet pattern using nested while:
A
AB
ABC
ABCD

1️⃣8️⃣ Print this number box pattern:
1111
2222
3333
4444

1️⃣9️⃣ Print this pattern:
1 1 1
2 2 2
3 3 3

2️⃣0️⃣ Print full pyramid using nested while:
    *
   ***
  *****
 *******
*********

'''

# 1️⃣ Print numbers from 1 to 20 using a while loop.
w = 1
while w <= 20:
    print(w)
    w=w+1


# 2️⃣ Print numbers from 50 to 1 (reverse) using a while loop.
w1 = 50
while w1 >= 1:
    print(w1)
    w1=w1-1

# 3️⃣ Print all even numbers between 1 and 100 using a while loop.
w2=1
while w2 <=100:
    if w2%2==0:
        print(w2)
    w2=w2+1

#4️⃣ Print all odd numbers between 1 to 100 using a while loop.
w3=1
while w3 <= 100:
    if w3%2!=0:
        print(w3)
    w3=w3+1

#5️⃣ Print multiplication table of a number using while loop.
w4=2
i=1
while i<=10:
    print(w4,'x',i,'=',w4*i)
    i=i+1

'''
6️⃣ Find the sum of digits of a number using a while loop.
Example → 123 → 1+2+3 = 6
'''
digit = 123
sum = 0
while sum > 0:
    print(sum)
    sum = sum + digit

'''
7️⃣ Reverse a number using while loop.
Example → 123 → 321
'''
w5=3
while w5 >= 1:
    print(w5,end='')
    w5=w5-1

#8️⃣ Count digits in a number using while loop.
w6=int(input('Enter a number:- '))
count = 0
while count > 0:
    count = w6 + count
print(count)
count = count + 1

''' 9️⃣ Keep taking input until user enters 0, then stop.
user = input('Enter a something:- ')
while user:
    if user == 0:
        print(user)
    elif user == 'stop':
        break'''

# 🔟 Guessing game: keep asking for password until user enters correct one.

'''
1️⃣1️⃣ Print this pattern using nested while:
*
**
***
****
'''
s=1
while s<=4:
    s1=1
    while s1<=s:
        print('*',end=' ')
        s1=s1+1
    print()
    s=s+1


''''
1️⃣2️⃣ Print this pattern:
****
****
****
****

'''
a=1
while a<=4:
    a1=1
    while a1==a:
        print('*',end='')
        a1=a1+1
    print()
    a=a+1