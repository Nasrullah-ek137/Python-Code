# access character in str

# a) index
a="Hello world Shanuuuuuue"

print(a[1]) # e
print(a[5]) # 
print(a[12]) # S
print(a[16]) # u
print(a[-1]) # e

# b) slicing     end number ek extra dena rahta hai

a1="Hello shanu how are youuuuuuuuuuuuu"

print(a1[0:5]) # Hello 
print(a1[6:11]) # shanu
print(a1[:])  # Hello shanu how are youuuuuuuuuuuuu
print(a1[5::2])

print(a1[6].upper()+a1[7:11])



# Mathematical operator
# a) + opr
a='Hello'
a1='Shanu'
print(a + a1 + 'Bhai')

# b) * opr
a='hello'
print(a * 2)

# Membership opr in , not in
s='Hello how are you hdiesklsl'
print('H' in s)

print('x' in s)

print('x' not in s)

print('h' not in s)


# Comprison opr and equality opr
s="Hello world"
s1="Hello shanu"

print(s == s1)
print(s != s1)
print(s > s1)
print(s >= s1)
print(s < s1)
print(s <= s1)

# Changing case name
s = "Hello Shanu bhai"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

# Count substring
s = "Hello world how are you sakdhfeuxdk"
print(s.count('h'))
print(s.count('h',6,))

print(s.count('o',1,23))

# find substring
s = "Hello world how are you sakdhfeuxdk"
print(s.find('h'))

print(s.rfind('s'))

print(s.index('s'))

print(s.rindex('w'))

# removing space from str
s="                        hello              bhai                 "
print(s)

s1 = s.lstrip()
print(s1)

s2 = s.rstrip()
print(s2)

s3 = s.strip()
print(s3)


# replace
s="Hello world python langauge is too difficult to learn"

s1 = s.replace('difficult','Easy')
print(s1)

# splitt
s="Hello Shanu Bhai"

s1=s.split( )
print(s1)

# Joinnn
s=("15","06","2004")
s1=','.join(s)
print(s)


# starting and ending part of str
s="Hello world python langauge is too difficult to learn"

s1 = s.startswith('Hello')
print(s1)

s2= s.endswith('learn')
print(s2)

# to check type of caharacter present..
s = "shanu1137"
s1='shanu'
s2=123456
s3='SHANUU'
s4='Shanuu'
print(s.isdigit())
print(s.istitle())
