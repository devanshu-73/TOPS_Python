
# l1 = [3,42,[24,232,243,[43,3],2,54],54,54]

# print(l1[2][3][0])

# l1 = [3,54,5,3,4,5,64,78]
# l2 = []
# for i in range(len(l1)-1):
#     for j in range(len(l1)-1):
#         if(l1[i] == l1[i+1]):
#             if(i == j):
#              l1.remove(l1[i])
#              print("removed : ",)

# print("L1 : ",l1)


# task....
# l1 = [12,3.434,45,"hello",74,34.54,"happy",'alpha']
# str1 =[]
# ints = []
# floats = []

# for i in l1:
#     if(isinstance(i,str)):
#         str1.append(i)
#     elif(isinstance(i,int)):
#         ints.append(i)
#     elif(isinstance(i,float)):
#         floats.append(i)
# print("string : ",str1)
# print("int : ",ints)
# print("float : ",floats)




# task
# user choose value from list and computer pick one value from list 

import random
l1 = [12,45,343,545,5,6,4,7]
# user = [343,545,5,6]
# computer = [12,45,4,7]
user_score = 0
computer_score = 0

for i in range(5):
    print(f"--> Round {i+1} Start")
    lucky = random.choice(l1)
    print(f"--> lucky {i+1} : ",lucky)
    print("Select Your Choice From This List : \n",l1)
    user = int(input("--> Enter Your Choice : "))
    computer = random.choice(l1)
    print("--> Computer Choice : ",computer)

    if lucky ==  user:
        user_score+=1
        l1.remove(lucky)
    elif lucky == computer:
        computer_score+=1
        l1.remove(lucky)
    print("----------------------------------")
    print(f"--> Round {i+1} End")
    print("--> User Score : ",user_score)
    print("--> Computer Score : ",computer_score)
    print("============================================")

    
if(user_score>computer_score):
    print("**** User Wins ****")
else:
    print("**** Computer Wins ****")

print("Total User Score : ",user_score)
print("Total Computer Score : ",computer_score)











