sentence = input("Enter Sentence : ")

list1 = sentence.split(" ")
print("LIST1 :",list1)
count=0
dict1={}
for i in range(len(list1)):
    for item in list1[i:]:
        count=count+1
        dict1["item"]=count
print("Dict1 :",dict1)