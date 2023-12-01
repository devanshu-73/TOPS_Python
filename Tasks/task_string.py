str1 = input("enter string1 : ")
character = input("enter character : ")

count = 0
doesnot_exist = 0 
for i in str1:
    if character == i:
        count = count+1
    else:
        doesnot_exist = doesnot_exist+1 

print("count : ",count)
print("doesnot_exist : ",doesnot_exist)
