str1="Good afternoon"

# .spilt() : it will divide string into smaller chunks will return list string chunks

var = str1.split(' ')

print(var)

count=0
for i in var:
    count+=1

print("word count : ",count)

print(type(var))
