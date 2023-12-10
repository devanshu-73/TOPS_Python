# Task - 1 ==> Split Task

str1 = input("Enter String : ")

str2 = str1.split(" ")

count = 0 
for i in str2:
    count = count +1

print(count)

# Task - 2 ==> Find Char exists in string or not

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
