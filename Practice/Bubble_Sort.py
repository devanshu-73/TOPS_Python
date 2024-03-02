# a.sort()  # Existing list
# b= sorted(a)  # New list
# a = [55,22,33,44,11]
a = [5,3,1,4,2]

# bubble Sort
for i in range(len(a)):
    for j in range(0,len(a)-i-1):  # len(a)-1 will also work but unwanted comparision happens so interpreter work slow
        # print("a[j] , a[j+1] :",a[j],a[j+1])
        print("Before :",a)
        if a[j] > a[j+1]:
            # print("2) a[j] , a[j+1] :",a[j],a[j+1])
            a[j],a[j+1] = a[j+1],a[j]
            print("After : ",a)

print("Final :",a)