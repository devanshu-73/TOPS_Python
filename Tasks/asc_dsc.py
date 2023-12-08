# ascending order

li=[51,1,2,9,98,46,37,71]

for i in range(len(li)):
    for j in range(i,len(li)):
        if(li[i]>li[j]):
            li[j]=li[i]+li[j] # a = b+a
            li[i]=li[j]-li[i] # b = a+b
            li[j]=li[j]-li[i] # a = a+b
print(li)
        
# # descending order

# for i in range(len(li)):
#     for j in range(i,len(li)):
#         if(li[i]<li[j]):
#             li[j]=li[i]+li[j]
#             li[i]=li[j]-li[i]
#             li[j]=li[j]-li[i]
# print(li)

