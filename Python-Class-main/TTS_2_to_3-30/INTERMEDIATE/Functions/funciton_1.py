#with return type w/o parameters


def fun():
    num=int(input("Enter num : "))

    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(fun())
    
#with return type with parameters
def add(x,y):
    return x+y

print(add(12,5))
