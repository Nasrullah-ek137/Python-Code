a=10
print(a)
print(type(a))

b=20.5
print(b)
print(type(b))

c=True
print(c)
print(type(c))

d=1+2j
print(d)
print(type(d))
print(d.real)
print(d.imag)

e='HELLO WORLDDD'
print(e)
print(type(e))

f=[10,20,30,40,50]
print(f)
print(type(f))

g=(10,20,30,'hello',40)
print(g)
print(type(g))

h={'A':10,'B':20,'C':30}
print(h)
print(type(h))
print(h.keys())
print(h.values())

i=set()
print(i)
print(type(i))

print()

# Convert one datatype to another datatype..
a=10
b=float(a)
print(b)
print(type(b))

a1=10.0
b1=int(a)
print(b1)
print(type(b1))

a2=1
b2=bool(a2)
print(b2)
print(type(b2))

a3=12
b3=complex(a3)
print(b3)
print(type(b3))

a4=10
b4=str(a4)
print(b4)
print(type(b4))

a5=[10,20,30,40,50]
b5=tuple(a5)
print(b5)
print(type(b5))