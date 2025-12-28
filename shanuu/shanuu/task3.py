# 1 create tuple of 6 numbers and print first,middle and last element

t = (10,20,30,40,50,60)

print(t[0])
print(t[3])
print(t[-1])

# 2 create dict with keys as subj name and values as marks print marks for two specific subjects
d = {'maths':80,'physic':70,'chemistry':60,'english':90}

print(d.get('maths'),d.get('english'))

print(d['chemistry'],d['english'])

# 3 create dict with emp detail and upd salary then add new key for dept
d1 = {'empname':'shane','age':21,'salary':2300}

d1['salary'] = 20000
print(d1)

d1.setdefault('Department','IT')
print(d1)

# 4 create dict 3 city name with population delete one entry and then clearall entry
d2 = {

    'city':{'mumbai','bangluru','pune'},
    'population':{'1cr','50lakhs','2crs'}
}

d2['city'][0]