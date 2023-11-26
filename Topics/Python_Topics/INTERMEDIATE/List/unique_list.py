l1=[]


for i in range(10):
    num=int(input(f"Enter num {i+1} : "))
    l1.append(num)

print(l1)

ul=[]

for element in l1:
    if element not in ul:
        ul.append(element)


print("Unique list : ",ul)
