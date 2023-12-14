class Sample:
    def __init__(self,x,y):
        self.n1=x
        self.n2=y

    def mul(self):
        print("product : ",self.n1*self.n2)

# Sample class inherited here in Child
class Child(Sample):
    def display_child(self):
        print("data from Sample : ",self.n1)


o1 = Child(12,4)

o1.mul()
o1.display_child()
