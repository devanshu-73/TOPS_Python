# solution 1 With Dunder/Magic Method

class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __eq__(self,value):
        return(self.a == value.a and
        self.b == value.b)
a1 = A(12,4)
a2 = A(12,4)

print(a1==a2)

# solution 2.1 Without Dunder/Magic Method

# class A:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def addition(self,value):
#         return(self.a == value.a and
#         self.b == value.b)
# a1 = A(12,40)
# a2 = A(12,4)

# print(a1.addition(a2))

# solution 2.2 Without Dunder/Magic Method

# class A:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def addition(self,value):
#         if(self.a == value.a and self.b == value.b):
#             return True
#         else:
#             return False
# a1 = A(12,4)
# a2 = A(12,4)

# print(a1.addition(a2))