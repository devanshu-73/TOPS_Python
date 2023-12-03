'''
l1=[12,54,76,76.5]

str1="Heya Hope You're Fine"

t1=3,78,4,35
'''

#operator overloading

'''
a,b=12,3
print(a+b)

print("hello"+"world")
print("One "*3)'''

class Sample:
    def __init__(self,x):
        self.num=x

    def __add__(self,new_obj):    
        return self.num+new_obj.num

o1=Sample(12)
o2=Sample(4)

print(o1+o2)


# method overloading

'''
print(len(l1))
print(len(str1))
print(len(t1))
'''
