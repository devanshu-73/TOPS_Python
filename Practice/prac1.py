d = {'name':None,'amount':None}
while True:
    menu = '''
        Tops Bank
        Press 1 To Create Account
        Press 2 To Withdrawl Amount 
        Press 3 To Exit 
    '''
    print(menu)
    ch = int(input("enter Your Choice : "))
   
    if ch == 3:
        break
    elif ch == 1:
        name = input("Enter Your Name : ")     
        amount = int(input("Enter Amount : "))
        d['name']= name   
        d['amount']= amount   
    elif ch == 2 :
        name = input("Enter Your Name : ")     
        if name == d["name"] :
            print("Your Total Balance : ",d["amount"])
            amt = int(input("Enter Amount To Withdrawl : "))
            d["amount"] = d["amount"]-amt
            print("Withdrawl Successfully and Your Total Balance : ",d["amount"])
            break
        elif name != d["name"]:
            print("Account Does not Exists... ")
            
# str1 = "devdev dev dev"
# d = {}
# for i in str1:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)