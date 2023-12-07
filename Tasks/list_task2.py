list1 = []

while True:
    list_elem = input("Enter Input....(or -> enter 'stop' for finish) : ")
    if list_elem.lower() == "stop":
        break
    if list_elem.isdigit():
        list1.append(int(list_elem))
    else:
        print("Invalid Input..")

print("List1 :",list1)