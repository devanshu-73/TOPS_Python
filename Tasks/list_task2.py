# Write a Python program that takes a list of numbers as input and prints the sum of all the even numbers.
list1 = []
sum = 0
while True:
    list_elem = input("Enter Input....(or -> enter 'stop' for finish) : ")
    if list_elem.lower() == "stop":
        break
    if list_elem.isdigit():
        list1.append(int(list_elem))
    else:
        print("Invalid Input..")

print("List1 :",list1)

for item in list1:
    if item % 2 == 0:
        print("item = ",item)
        sum = item+sum
print("sum",sum)