# list Task-1 ; take 10 input and odd even counting


# task-1 :
# l1 = []
# n = int(input("enter element : "))
# for i in range(n):
#     num = int(input(f"enter number {i+1} : "))
#     l1.append(num)
    
# even_list = []
# odd_list = []
# even=0 
# odd=0 
# for j in range(n):
#     if l1[j]%2 == 0 :
#         even_list.append(l1[j])
#     else:
#         odd_list.append(l1[j])
# print("even : ",even_list)
# print("odd : ",odd_list)

# list task-2 : reverse the string without sort() method sort (reverse = True)

# =============================================================
# solution : 1
# str1 = "hello world"
# str2 = str1[::-1]

# print(str2,type(str2))
# =============================================================
# solution : 2

str1 = "hello world"
str2 =""
for i in str1:
    str2 = str2+i
print(str2)
    