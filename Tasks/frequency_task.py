# Frequency Task
# code 1

sentence = input("Enter Sentence : ")
list1 = sentence.split(" ")
print("LIST1 :",list1)
dict1={}

for item in list1:
    count=0
    for other_item in list1:
        if item == other_item:
            count=count+1
    dict1[item]=count
print("Dict1 :",dict1)


# code 2
from collections import Counter 
sentence = input("Enter Sentence : ")

list1 = sentence.split(" ")
dict1 = Counter(list1)
print("Dict1 :",dict1)
