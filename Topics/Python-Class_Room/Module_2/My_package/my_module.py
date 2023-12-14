def sum(x,y):
    return x+y

def mul(x,y):
    return x*y


def fact(num):
    if num>0:
        return num*fact(num-1)
    else:
        return 1
