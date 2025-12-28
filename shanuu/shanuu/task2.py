# 1 create list of color append 2 new color and remove one existing color
# 2 create list of 5 integer and insert new number at second position and remove last element
# 3 assign value to varable for the cost of 3 items and calculate total and avg cost.




# 1 create list of color append 2 new color and remove one existing color
l=['red','blue','grey']

l.append('black')
l.append('white')
print(l)

l.remove('red')
print(l)


# 2 create list of 5 integer and insert new number at second position and remove last element
l1 = [10,20,30,40,50]

l1.insert(1,15)
print(l1)

l1.pop()
print(l1)


# 3 assign value to varable for the cost of 3 items and calculate total and avg cost.
a = 10
b = 20
c = 30
print(a+b+c)



# 4 create list of number sort in asc order, then reverse the order
l = [20,40,50,30,10,60]

l.sort(reverse=False)
print(l)

# BOTH ARE ASC ORDER

l.sort()
print(l)


# REVERSE ORDER
l.sort(reverse=True)
print(l)

