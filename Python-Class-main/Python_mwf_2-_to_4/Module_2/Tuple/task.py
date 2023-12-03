# find nique list from the given

l1=[12,34,45,56,67,78,89,12,34]

unique_list=[]

for element in l1:
    if element not in unique_list:
        unique_list.append(element)


print("Unique List : ",unique_list)
