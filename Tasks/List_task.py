# task : 1

# Enter num : 2

# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 10 = 20

# n = int(input("Enter Number : "))
# for i in range(1,11):
#     print(n,"*",i," = ",n*i)

# ==========================================================================
# task : 2

# $ * * * * 
# * $ * * * 
# * * $ * * 
# * * * $ * 
# * * * * $

# n = int(input("Enter How Many Rows do u Want : "))
# for i in range(n):
#     for j in range(n):
#         print("$" if(i == j) else "*",end=" ")
#     print()

# ==========================================================================
# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     print("* " * i)

# ==========================================================================
# 1
# 1 0
# 1 0 1
# 1 0 1 0

# n = int(input("Rows : "))

# for i in range(n):
#     for j in  range(i+1):
#         print(1 if(j%2 == 0) else 0,end=" ")
#     print()
# ==========================================================================
# 1
# 2 3
# 4 5 6 
# 7 8 9 10

# row = int(input("enter row : "))

# k = 1
# for i in range(row):
#     for j in range(i+1):
#         print(k,end=" ")
#         k+=1
#     print()
# ==========================================================================
# A 
# B C
# D E F 
# G H I J
# K L M N O

# row = int(input("enter row : ")) 
# char_num = ord('A')
# for i in range(row):
#     for j in range(i+1):
#         print(chr(char_num),end=" ")
#         char_num+=1
#     print()

# ==========================================================================
# A
# A B 
# A B C
# A B C D
# A B C D E

# row = int(input("Enter Rows : "))
# char_num = ord('A')
# for i in range(row):
#     for j in range(i+1):
#         print(chr(char_num+j),end=" ")
#     print()    

row = int(input("Enter Rows : "))
char_num = ord('A')

for i in range(row):
    for j in range(i + 1):
        print(chr(char_num), end=" ")
        char_num += 1
    print()

#  print(string.ascii_uppercase[j], end=" ") but u have to import string module

# ==========================================================================
# 	      *
#       * *
#     * * *
#   * * * *
# * * * * *

# * * * * * 
# * * * * 
# * * *
# * *
# *

#     *
#    * *
#   * * *
#  * * * * 
# * * * * * 

# * * * * *
#  * * * *
#   * * * 
#    * *
#     *
