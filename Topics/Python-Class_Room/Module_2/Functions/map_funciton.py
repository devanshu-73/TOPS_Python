# map() : apply function to each element of collection
# Syntax : map(fun,iterable)

def double(x):
    return x*x

l1=[1,2,3,4,5]

print(list(map(double,l1)))
