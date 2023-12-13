# Task : 2

# ===========Choice Board===========

	# 1. Addiiton
	# 2. Substraction
	# 3. Multiplication
	# 4. Division
	# 5. Modulo
	# 6. Exit

# 	Enter Your Choice : 2
	
# 	Enter two numbers : 12
# 	6
# 	Your Ans : 6

# 	Do You Want to continue ? ['y/n']: 
	
# 	if n:
# 	Thank You

# 	if y
# 	repeat the process 


print("===========Choice Board===========")

print("1. Addiiton")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Exit")

choice = int(input("Enter Your Choice : "))
if(choice == 1):
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    print("Addition :",a+b)
elif(choice == 2):
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    print("Substraction :",a-b)
elif(choice == 3):
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    print("Multiplication :",a*b)
elif(choice == 4):
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    print("Division :",a/b)
elif(choice == 5):
    a = int(input("Enter No 1 : "))
    b = int(input("Enter No 2 : "))
    print("Modulo :",a%b)
elif(choice == 6):
    exit()
else:
    print("U Entered Wrong Choice ")

