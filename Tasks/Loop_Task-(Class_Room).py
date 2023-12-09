# ==========================================================================

# Task - 1 Print Hello 10 Times
 
# for i in range(1,11):
#     print(i,") Hello",sep="")

# ==========================================================================

# Task- 2 Sum of till N positive number

# sum=0
# for i in range(1,11):
#     n = int(input("enter number : "))
#     sum = sum+n
 
# print("Addition :",sum)

# ==========================================================================

# Task - 3 Odd Even Counting

# count_even = 0
# count_odd = 0
# for i in range(10):
#     n = int(input("enter number : "))
#     if((n%2) == 0):
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1

# print("Even :",count_even)
# print("Odd :",count_odd)

# ==========================================================================

# Task 4 Pattern

#       * * * * * 
#       * * * * * 
#       * * $ * * 
#       * * * * * 
#       * * * * * 

# for i in range(5):
#     for j in range(5):
#         if(i == 2 and j == 2):
#             print("$",end=" ")
            
#         else:
#             print("*",end=" ")
#     print()

# ==========================================================================

# Task 5 Pattern

#       $ * * * * 
#       * $ * * * 
#       * * $ * * 
#       * * * $ * 
#       * * * * $ 

# for i in range(5):
#     for j in range(5):
#         if(i == j):
#             print("$",end=" ")
            
#         else:
#             print("*",end=" ")
#     print()

# ==========================================================================

# Task : 6 Pattern

#       * 
#       * *       
#       * * *     
#       * * * *   
#       * * * * * 

# for i in range(1,6):
#  { 
#    print("* " * i)
#  }

    
# ==========================================================================

# Task : 7

# Enter num : 2

# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 10 = 20

# n = int(input("Enter Number : "))
# for i in range(1,11):
#     print(n,"*",i," = ",n*i)

# ==========================================================================

# Task : 8

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

# Task : 9

# * 
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     print("* " * i)

# ==========================================================================

# Task : 10

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

# Task : 11

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

# Task : 12

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

# Task : 13

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


#  print(string.ascii_uppercase[j], end=" ") but u have to import string module

# ==========================================================================
