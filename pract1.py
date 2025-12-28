'''
3️⃣ Reverse a string without slicing or reversed().
4️⃣ Check if a number is palindrome.
5️⃣ Print Fibonacci series up to n terms.
6️⃣ Count digits in a number.
7️⃣ Find the largest and second largest number in a list.
8️⃣ Remove duplicates from a list.
9️⃣ Find frequency of each word in a sentence.
🔟 Check whether a number is prime.'''

# 1️⃣ Write a program to print sum, difference, product, and division of two numbers.
class Program:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def difference(self):
        return self.a-self.b
    def product(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
pr=Program(50,23)
print(pr.sum())
print(pr.difference())
print(pr.product())
print(pr.division())

# 2️⃣ Count vowels and consonants in a string.
'''class vowels:
    count=0
    def strvowels(string):
        l=['a','e','i','o','u']
        if l in string:
            vowels.count += 1
        print(vowels.count)
vo=vowels
vo.strvowels('shanuuers')'''


'''
B. LOOPS (For / While)

1️⃣ Print all numbers divisible by 3 and 7 between 1–200.
2️⃣ Find sum of digits of a number using while loop.
3️⃣ Print multiplication table of a number using loop.
4️⃣ Print star pattern:

*
**
***
****
5️⃣ Print full pyramid using loop.
6️⃣ Reverse a number using loop.
7️⃣ Print all even numbers from a list.
8️⃣ Print matrix 3×3 using nested loop.
9️⃣ Input numbers till user enters 0 → count positives.
🔟 Print prime numbers from 1 to 100.'''

# 1️⃣ Print all numbers divisible by 3 and 7 between 1–200.
def number():
    for i in range(1,201):
        if i%3==0 and i%7==0:
            print(i)
number()

# 2️⃣ Find sum of digits of a number using while loop.
summ=0
s=1
while s > 10:
    summ=summ+s
    s=s+1
print(summ)

'''
C. FUNCTIONS (Normal + args + kwargs)

1️⃣ Write a function to return factorial of a number.
2️⃣ Write a function to print all vowels in a string.
3️⃣ Write a function using *args to return maximum number.
4️⃣ Write a function using **kwargs to print employee details.
5️⃣ Write a function that uses both *args and **kwargs.
6️⃣ Write SI function with default parameters.
7️⃣ Write a function to count words in a string.
8️⃣ Write a function power(num, exponent=2).
9️⃣ Write a function greet(name="Guest").
🔟 Write a function to reverse string using loop.

🔥 D. LAMBDA / MAP / FILTER / REDUCE

1️⃣ Use lambda to square a number.
2️⃣ Use map() to convert list of numbers into squares.
3️⃣ Use filter() to filter even numbers from a list.
4️⃣ Use reduce() to find sum of a list.
5️⃣ Sort list of tuples by second element using lambda.
6️⃣ Use lambda to sort names by last letter.
7️⃣ Use filter to get names starting with "A".
8️⃣ Use map to convert all names to uppercase.
9️⃣ Use lambda to multiply two numbers.
🔟 Use reduce to find maximum element.'''


'''
'''

