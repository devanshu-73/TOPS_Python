'''
Tuple : Collection in python which hold mutiple elemenst of different type

represented with : ()

in-built class : tuple()

Characteristics:

    - Tuples are immutable/hashable/unchangable
    - Tuples are orderable
    - are indexible
    - they are iterable

>>IMP:

Difference between tuple & list

'''
#blank tuple
t1=()
t2=tuple()

print(type(t1))
print(type(t2))

print(hash(t1))
print(hash(t2))


print("Tuple : 3")
t3=(12,34,'Hola',39.3)
print(t3)
print(type(t3))

print("Tuple : 4")
t4=(23,)
print(t4)
print(type(t4))

print("Tuple : 5")
t5=12,34,"hello",37.8
print(t5)
print(type(t5))















