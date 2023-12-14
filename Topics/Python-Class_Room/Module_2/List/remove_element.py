# methods to remove elements from the lsit

'''
.pop():
    w/o index will remove last elemet
    with index will remove specific element by position

.remove(): will remove by element itself

del : remove specificc indexed element

.clear(): will remove all elements from lsit


'''


l1=[12,34,5,65,7,67,87,23,12,43,6]


print("List Sorting ")

l1.sort()


print("In asc : ",l1)

l1.sort(reverse=True)

print("In desc : ",l1)

l1.remove(12)

del l1[-2]


l1.clear()

print(l1)












