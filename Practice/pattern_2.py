n = int(input("Enter Number : "))

for i in range(n):
    for j in range(n):
        if(j<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# n = int(input("Enter Number : "))

# for i in range(5):
#     for j in range(5):
#         if(j<=i):
#             if ((i+j)%2 == 0):
#                 print(1,end=" ")
#             else:
#                 print(0,end=" ") 
#     print()

n = int(input("Enter Number : "))
for i in range(n):
    for j in range(i + 1):
        print(1 if (i + j) % 2 == 0 else 0, end=" ")
    print()

# for i in range(5):
#     for j in range(i+1):
#         if((i+j)%2 == 0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()
    
# for i in range(1,6):
#     row_values = " ".join("0" if (i + j) % 2 == 0 else "1" for j in range(i))
#     print(row_values)
