# Access element of tuple

# a) by using index
t=(10,20,30,40,'hello',50,60,'world')
print(type(t))

print(t[4][4])
print(t[-1][-5])
print(t[6])

# b) by using slicing 
print(t[1:4])
print(t[0::2])
print(t[4::3])

# Mathematical opr +,*
t=(10,20,30,40,50,'hello',60,70,'world')
print(t+(10,))
print(t+(100,90,80,70,60))

print(t*2)


# IMP function in tuple
t=(10, 20, 30, 40, 50, 'hello', 60, 70, 'world', 10, 20, 30, 40, 50, 'hello', 60, 70, 'world')
print(len(t))

print(t.count(10))
print(t.count(60))

print(t.index(50))
print(t.index('world'))
