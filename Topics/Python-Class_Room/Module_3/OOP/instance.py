class A:
    def display(self):
        print("hello all from A")


class B:
    def display(self):
        print("Hello all from B")


a1=A()
b1=B()

print(isinstance(b1,A))



num=23
print(isinstance(num,int))

str1="hello"
print(isinstance(str1,str))
