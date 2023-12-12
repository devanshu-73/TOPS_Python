# Task : 3

# =============Area Finder=============

# 	1. Circle
# 	2. Triangle
# 	3. Rectangle 

# 	Enter Choice : 3
	
# 	Enter length : 
# 	Enter Width : 
# 	Area of Rectangle : 
	
# 	>>>>>>>>>>>>>Thank You 


print("=============Area Finder=============")
print("   1. Circle")
print("   2. Triangle")
print("   3. Rectangle")
choice = int(input("Enter Your Choice : "))
if(choice==1):
    r = int(input("Enter radius of circle : "))
    area = 3.14 * r * r
    print("Area Of Circel :",area)
    print(">>>>>>> Thank You <<<<<<<")
elif(choice==2):
    b = int(input("Enter Base of Triangle : "))
    h = int(input("Enter Height of Triangle : "))
    area = (1/2)*b*h
    print("Area Of Triangle :",area)
    print(">>>>>>> Thank You <<<<<<<")
elif(choice==3):
    l = int(input("Enter Length of Rectangle : "))
    w = int(input("Enter Width of Rectangle : "))
    area = l*w
    print("Area Of Rectangle :",area)
    print(">>>>>>> Thank You <<<<<<<")
else:
    print("U Entered Wrong Choice...")
