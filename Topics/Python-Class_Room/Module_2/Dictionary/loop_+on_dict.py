# dictionary is iterable

d1={'name': 'Nikhil', 'age': 12, 'gender': 'male'}

# .keys() : it return only keys from dict
# .values() : it returns only value from dict
# .items() : return pair of key and value

for element in d1.items():
    print(element)
    print(type(element))


# .clear() : remove all the elements
# .copy() : copy dict to another
# .update() : will update existing dict with new one


d2=d1.copy()

d1.clear()

del d2['gender']
d2['name']="Smit"

print(d1)
print(d2)
