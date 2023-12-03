'''
Set : Collection of mutiple non-duplicate elements in unordered form

represents with : {}
in-built class : set()

characteristics:
- it is unorderable
- only accept unique elements
- not indexed
- it is iterable

'''

s2={} #this is wrong set declaration will give dict() as type

s1={12,45,'hey',12,45,46,67}
print(type(s1))
print(s1)

#hence set() are iterable in python
for i in s1:
    print(i)









