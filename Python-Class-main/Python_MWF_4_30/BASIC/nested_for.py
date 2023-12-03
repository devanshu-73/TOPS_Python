#Nested Loop
print(">>>pattern : 1")
for x in range(5):
    for i in range(5):
        print("*",end=" ")
    print()

    
print(">>>pattern : 2")
for x in range(1,6):
    for i in range(1,x+1):
        print("*",end=" ")
    print()

print("<<<<<pattern")
for x in range(1,11):
    print("* "*x)


print("<<<<<pattern")
for x in range(1,11):
    print(' '*(10-x)+" *"*x)




















 




