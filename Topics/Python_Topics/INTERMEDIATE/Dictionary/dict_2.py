# how to access elements in dict
d1={
    'k1':1,
    'k2':2,
    'k3':3
    }

print("Before")
print(d1)
print(id(d1))

d1['k1']=34
print(d1['k1'])

print("After")
print(d1)
print(id(d1))


