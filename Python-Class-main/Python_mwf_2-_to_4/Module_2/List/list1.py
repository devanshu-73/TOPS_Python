'''
    List : "Collection of different type of data elements"


    represents with : []

    in-built class : list()

    >>Characteristics :

    Lists are indexible : index starts from zero
    Lists are iterable
    They are mutable/Changable
    it support -ve indexing
    It allow duplicaption of elements


'''

# blank list declaration

l1=list()
l2=[]
l3=[12,'d',23.4,"Hello",32]

print("List 3 : ",l3)
print("List 1 : ",l1)
print(type(l3))

for i in l3:
    print(i)

# access list elements

print(l3[3])
print(l3[1:4])

print(l3[::-1]) # will reverse the list


print(type(l1))
print(type(l2))
















