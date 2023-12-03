status=True

while(status):
    num=int(input("Enter num : "))

    if num%2==0:
        print("Even")
    else:
        print("Odd")

    ch=input("Do You want to continue ? ['y/n'] : ")
    if ch=='Y' or ch=='y':
        status=True
    else:
        status=False
