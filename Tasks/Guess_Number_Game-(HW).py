import random

status = True

while(status):

    lucky = random.randint(1,100)
    print(lucky)
    chance = 5
    user = int(input("Enter your Num : "))

    while (chance>0):
        if (user>lucky):
            print("Too Large")
            user = int(input("Enter your Num : "))
        elif (user<lucky):
            print("too small")
            user = int(input("Enter your Num : "))
        elif (user == lucky):
            print("got it")
            break
        
        chance=chance-1
        print("chances : ",chance)
        
    user_intr=input("Do u wanna play again...? [y/n]")
    if(user_intr == "y" or user_intr == "Y"):
        status=True
    else:
        status=False
                        
