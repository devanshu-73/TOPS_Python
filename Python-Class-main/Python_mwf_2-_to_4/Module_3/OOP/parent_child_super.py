class Sample:
    def __init__(self,x):
        self.p=x
    def displayP(self):
        print("in parent : ",self.p)

# Sample class inherited here in Child
class Child(Sample):
    def __init__(self,u):
        super().__init__(23)
        super().displayP()
        self.c=u

    def displayC(self):
        print("in child : ",self.c)


c1=Child(32)
c1.displayC()
