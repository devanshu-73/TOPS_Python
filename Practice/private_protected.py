# ==================== Encapsulation ====================      

class A:
    public = 30
    __private = 20
    _protected = 10
    def show(self):
        return (100+110)
    # print("Protected : ",_protected)
    # print("Private : ",__private)
    
    
a = A()
print("public : ",a.public)
print("protected : ",a._protected)
print("private : ",a._A__private)

# 2nd Way 
# we can access variable using className
# Can't access Function using className
print("public : ",A.public)
print("protected : ",A._protected)
print("private : ",A._A__private)