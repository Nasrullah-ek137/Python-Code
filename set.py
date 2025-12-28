s={10,20,30,40,50,60,70}

print(type(s))

print(s)

# Equality oprr
s={10,20,30,40,50,60,70}
s1={10,30,60,50,30}
print(s == s1)

print(s != s1)


# Membership opr...
s={10,20,30,40,50,60,70}
print(10 in s)
print(100 in s)

print(100 not in s)
print(20 not in s)

# add element
s={10,20,30,40,50,60,70}
s.add(80)
print(s)

s.update({60,70},{80,90})
print(s)

# delete
s={70, 40, 10, 80, 50, 20, 90, 60, 30}
s.pop()
print(s)

s.remove(90)
print(s)

s.discard(60)
print(s)

s.clear()
print(s)


