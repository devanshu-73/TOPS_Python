#returning lambda from another funciton


def double(x):
    return lambda r,t : r*x*t

fun = double(10)
print(fun(20,8))
