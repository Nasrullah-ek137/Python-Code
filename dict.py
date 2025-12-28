# Delete element in dict

d = {'A':10,'B':20,'C':30,'D':40,'E':50}
print(d)

print(d.keys())
print(d.values())
print(d.items())

print(d['A'])

d1 = d['D'] = 35
print(d1)

print(d)

del d['E']
print(d)

d3 = {'A':10,'B':20,'C':30,'D':40,'E':50}

d4 = d['A'] == d['B']
print(d4)


d5 = d['C'] != d['B']
print(d5)


dd = {'A':10,'B':20,'C':30,'D':40,'E':50}

de = 'B' in dd
print(de)

dde = 'F' not in dd
print(dde)


# imp function 
dz = {'A':10,'B':20,'C':30,'D':40,'E':50}
print(len(dz))

print(dz.get('A'))

print(dz.get('F',600))

print(dz.popitem())

d1 = {'A':10,'B':20,'C':30}
d2 = {'D':40,'E':50}

d3 = {**d1 , **d2}
print(d3)

l=[10,20,30,40]
s=dict.fromkeys(l,'hello')
print(s)



dict1 = {
    'student': {'name': 'shanu', 'age': 21, 'gender': 'male'},
    'detail': {'course': 'python', 'duration': '6 months'},
    'other': {'address': 'govandi', 'pincode': 400043}
}
print(dict1['student']['name'],' ',dict1['other']['address'])
