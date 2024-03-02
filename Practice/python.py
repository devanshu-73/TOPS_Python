# a.sort()  # Existing list
# b= sorted(a)  # New list
a = [5,6,4,2,7,1,3]


# bubble Sort
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)