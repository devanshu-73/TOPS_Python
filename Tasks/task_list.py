# list Task-1 ; take 10 input and odd even counting

# list task-2 : reverse the string without sort() method sort (reverse = True)


# task-1 :
l1 = []
n = int(input("enter n : "))
for i in range(n):
    num = int(input(f"enter number {i+1} : "))
    l1.append(num)
    
# even_list = []
even=0 
odd=0 
for j in range(10):
    if l1[j]%2 == 0 :
        even
# for i in range(10):
#     print(f"num {i} :",l1[i])