l1=[12,23,43,54,76]
l2=[23,546,6,5]
l3=[12,45,6,5]

print(list(zip(l1,l2,l3)))

for i,j,k in zip(l1,l2,l3):
    print(i)
    print(j)
    print(k)
    print()
