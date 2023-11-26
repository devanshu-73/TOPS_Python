l1=[12,34,54,57]

t1=(34,90,655,67,7)

print("before updation list : ")
print(l1)
print(id(l1))

l1[2]="hello"

print("after updation list : ")
print(l1)
print(id(l1))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("before updation tuple : ")
print(t1)
print(id(t1))

t1=(34,90,"Hello",67,7)

print("before updation tuple : ")
print(t1)
print(id(t1))
