'''
    Collection Tuple :

        "A collection in python that contain multiple type
        of different elemnts "


    represents with : ()
    n-built class : tuple()
    

    >>Characteristics :

    Tuples are immutable
    Tuuples are iterable
    They are indexible (-ve inidex support)   

'''

# single element in tuple : neccessary to put comma afetr
tx=("hello",)
print(type(tx))


t1=(12,23.3,"hello")
t2=12,"hey",23.4
print(type(t2))

print(t1)
print(t1[-1])
print(type(t1))


for i in t1:
    print(i)
