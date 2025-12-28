# Access element of list

# a) by using index
l=[10,20,30,40,50,[60,10,20,[30,40,60,90]],100]

print(l[4])
print(l[5][2])
print(l[5][3][2])
print(l[6])

# b) by using slicing     start : end-1 : step
l=[10,20,30,40,50,60,70,80,90,100,90,86,54,32]

print(l[0:5:1])
print(l[-5::])
print(l[0::2])



# Mathematical operator..

# a) + opr
l=[10,20,30,40,50,60,70]
l1=[80,90,100,90,86,54,32]
print(l + l1)

# b) * opr
l=[10,20,30,40,50,60,70]

print(l * 2)

# Comparison and relational opr..
l=['hello','bhai','kaise','hooo','aap']
l1=['How','areee','ypuuuuu','brooeoeoe','sdjeek']

print(l == l1)
print(l != l1)
print(l > l1)
print(l >= l1)
print(l < l1)
print(l <= l1)


# Membership opr..
l=[10,20,30,40,50,60,70]
print(10 in l)
print(80 in l)

print(100 not in l)
print(20 not in l)

# to get information about list
l=[10,20,30,40,50,60,70,10,20,30,40,50,10,10,20,30,10]
print(len(l))

print(l.count(10))

print(l.index(20))


# Manipualting element in list..
l=['A','B']
print(l.append('C'))
print(l)

print(l.insert(3,'D'))
print(l)

l1=['E','F','G']

print(l.extend(l1))
print(l)

# Removing
l=['A','B','C','D','E','F','G','H','I','J']

l.pop()
print(l)

l.pop(0)
print(l)

l.remove('D')
print(l)

l.clear()
print(l)

# Ordering element in list

# a) reverse()
l=[10,20,30,40,50,60,70,10,20,30,40,50,10,10,20,30,10]

l.reverse()
print(l)

l.sort(reverse=True)
print(l)