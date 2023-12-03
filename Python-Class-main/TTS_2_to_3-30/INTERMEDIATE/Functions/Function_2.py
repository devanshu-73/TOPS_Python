#w/o return type with parameters

# funciton creation 
def my_Function(value): # here value is formal parameter
    print("Value is : ",value)


#function calling

num=int(input("Enter number : "))

my_Function(num) # here num is actual parameter
print(my_Function("Hello"))

print(">>>>>>>>>>>>>>>>>>>>")
print(num)
print(value) # will give error as not defined 
