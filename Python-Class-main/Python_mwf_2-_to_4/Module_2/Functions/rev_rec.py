def my_fun(x):
    print(x)
    if x<=1:
        return 0
    else:
        return my_fun(x-1)

my_fun(10)
