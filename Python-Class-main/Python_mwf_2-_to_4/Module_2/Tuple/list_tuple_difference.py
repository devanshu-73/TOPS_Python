# difference between List & Tuple

# based on single element store

ln=[12]
print(type(ln))

tn=(34)
print(type(tn))

# based on breakets
l1=["hello",23]
t1="hello",34,6,34.4

print(type(l1))
print(type(t1))


#based on memory location

print("for List >>>>>>>>>>>")
lx=[12,23,45,56,78]
print("before chnage : ",id(lx))
lx[2]=843
print("after change : ",id(lx))
print(lx)


print("for tuple >>>>>>>>>>>>")
tx=12,34,5,667
print("before chnage : ",id(tx))
tx=12,34,65,667
print("after chnage : ",id(tx))

print(tx)
