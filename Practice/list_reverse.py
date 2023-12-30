l1 = [1,2,3,4,5,6,7,8]
l1.reverse()
print(l1)
l2=[]

l2 = l1[::-1]
print("l1 : ",l1)
print("l2 : ",l2)

# l1 = [1,2,3,4,5,6,7,8]
# start=0
# end=len(l1)-1
# while start<end:
#     l1[start] , l1[end] = l1[end] , l1[start]
#     start = start+1
#     end = end-1

# print(l1)