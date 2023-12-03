# overriding :

class Parent:
    def display(self):
        print("Hello from Parent")

class Child(Parent):
    def display(self):
        super().display() # to remove the problem overriding
        print("Hello from Child")


c1=Child()
c1.display()
