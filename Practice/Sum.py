# Sum of largest and smallest number

lis1 = []
num = int(input("Enter How Many Element do u Want ? : "))

for i in range(num):
    number = int(input(f"Enter Number {i+1} : "))
    lis1.append(number)

shorted_list = lis1.sort()

print(shorted_list)
# print(lis1[0]+lis1[-1])