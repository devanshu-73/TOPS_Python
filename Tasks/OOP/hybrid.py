class A:
        a = int(input("Enter A Value :"))
        b = int(input("Enter B Value :"))
class B(A):
    def addition(self):
        add = self.a+self.b
        return add
class C(A):
    def multi(self):
        mul = self.a*self.b
        return mul
class D(B,C):
    
    def __init__(self):
        print("A + B:",self.addition())
        print("A * B:",self.multi())
    
    
d_obj = D()