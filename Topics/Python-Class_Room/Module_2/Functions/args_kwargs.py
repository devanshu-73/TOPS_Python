print(">>>>>>>>>>>>>>>>>>args")

def fun1(*x): # args: arguments
    for i in x:
        print(i)

l1=[12,23,4,3,56]
x=23
k1=90
fun1(l1,x,k1)

print(">>>>>>>>>>>>>>kwargs")

def fun2(**x): # kwargs: keyword arguments
    for i,k in x.items():
        print(f'{i} = {k}')

fun2(l1=23,x=[12,43,5],k2=903)

