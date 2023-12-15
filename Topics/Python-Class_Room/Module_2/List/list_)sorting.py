l1=[]

c=int(input("how many elements you want : ? "))

for i in range(c):
    num=int(input("Enter element : "))
    l1.append(num)

for i in range(len(l1)):              #i = 0
    for j in  range(i+1,len(l1)):     #j = 1
        if l1[i]>l1[j]:               #l1[0] = l1[1]   
            l1[i],l1[j]=l1[j],l1[i]   #l1[0],l1[1] = l1[1],l1[0]

print(l1)
