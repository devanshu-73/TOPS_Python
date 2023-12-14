l1=[] # blank list

l2=list() # blank list

print(l1)
print(type(l1))
print(id(l1))

print(l2)
print(type(l2))
print(id(l2))


l1=[12,23.43,"hello",-384,True]

print("New List : ",l1)

for i in l1:
    print(i)

# List Slice

print(l1[1:3])

print(l1[::-1])

l1.reverse() # inplace change occur
print(l1)












