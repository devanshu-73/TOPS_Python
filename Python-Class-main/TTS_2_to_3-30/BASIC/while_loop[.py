'''
    initialization
    While condition:
        code..
        updation


    >>It is an Entry/Execution Control loop
'''
a=True

while a:
    num=int(input("enter num : "))

    if num%2==0:
        print("Even")
    else:
        print("Odd")

    choice=input("Want to continue ? ['y/n'] : ")
    if choice=='y':
        a=True
    else:
        a=False













    
