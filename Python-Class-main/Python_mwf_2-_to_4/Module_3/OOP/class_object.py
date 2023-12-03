#class creation 
class User:
    
    def input(self,x,y):
        self.age=x
        self.weight=y

    def display(self):
        print("age : ",self.age)
        print("weight : ",self.weight)


#object creation

obj1 = User()

obj1.input(12,43)
obj1.display()
