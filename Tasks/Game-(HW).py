
# task

# user choose value from list and computer pick one value from list 

import random
l1 = [12,45,5,6,4,7,343,41,73,90,78,545]
user_list = []
computer_list = []

for i in range(int(len(l1)/2)):
    random_element = random.choice(l1)
    if random_element not in user_list:
        user_list.append(random_element)

for i in l1:
    if i not in user_list:
        computer_list.append(i)
        
print("U :",user_list)
print("C :",computer_list)
    
user_score = 0
computer_score = 0

for i in range(5):
    print(f"--> Round {i+1} Start")
    lucky = random.choice(l1)
    print(f"--> lucky {i+1} : ",lucky)
    print("--> Computer List : ",computer_list)
    print("Select Your Choice From This List : \n",user_list)
    user = int(input("--> Enter Your Choice : "))
    computer = random.choice(computer_list)

    if lucky ==  user:
        user_score+=1
        user_list.remove(lucky)
    elif lucky == computer:
        computer_score+=1
        computer_list.remove(lucky)
    print("----------------------------------")
    print(f"--> Round {i+1} End")
    print("--> User Score : ",user_score)
    print("--> Computer Score : ",computer_score)
    print("============================================")
    print("--> Computer List : ",computer_list)
    print("--> User List : ",user_list)

    
if(user_score>computer_score):
    print("**** User Wins ****")
else:
    print("**** Computer Wins ****")

print("Total User Score : ",user_score)
print("Total Computer Score : ",computer_score)




