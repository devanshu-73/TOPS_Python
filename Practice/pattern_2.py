# n = int(input("Enter Number : "))

# for i in range(n):
#     for j in range(n):
#         if(j<=i):
#             print("*",end="1")
#         else:
#             print(" ",end="2")
#     print()

# n = int(input("Enter Number : "))

# for i in range(n):
#     for j in range(n):
#         if(j<=i):
#             if ((i+j)%2 == 0):
#                 print(1,end=" ")
#             else:
#                 print(0,end=" ") 
#     print()


for i in range(1,6):
    for j in range(i):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
