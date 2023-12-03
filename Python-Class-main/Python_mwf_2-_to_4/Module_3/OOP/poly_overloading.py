'''
    Polymorphism : "Having many forms"

    Types :

    1) Runtime (Overridding)
    2) Compile time (Overloading)

'''
# poly: method overloading (not possible in python)
'''
class Sample:

    def display(self,x):
        self.n1=x
        return f'{self.n1}'

    def display(self,x,y):
        self.n1=x
        self.n2=y
        return f'{self.n1} {self.n2}'

    def display(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
        return f'{self.a} {self.b} {self.c}'


o1=Sample()
print(o1.display(12,54,7))'''



'''
class Bird:
    def display(self,name1,name2="Donald",name3="None"):
        print("Name 1 : ",name1)
        print("Name 2 : ",name2)
        print("Name 3 : ",name3)


o1=Bird()

o1.display("Daisy")
o1.display("Goofy","Goose")
o1.display("one","two","three")
'''

















