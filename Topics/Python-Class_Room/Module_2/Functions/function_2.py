""""

Recursion : "calling of   own again and again"

recursive function : "A  funciton that call itself again and again is
                called as recursive funciton"

fact(x) = x*fact(x-1)

fact(0)=1
"""

def fact(x):
    if x<=0:
        return 1
    else:
        return x*fact(x-1)



print("factorial is : ",fact(5))
