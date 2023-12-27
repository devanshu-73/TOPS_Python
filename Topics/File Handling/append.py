# f = open("append.txt","a")

# append,write
# for i in range(1,4):
#     name = input("Enter Name : ")
#     f.write("\n"+name)
# f.close()

# ============================================

# read

# f = open("append.txt","r")
# d =f.read()
# d =f.readlines()
# d =f.readline()
# print("no of lines :",len(d))
# print(d)
# s =d.split() 
# print(s)
# =======================================


count = 0
f = open("append.txt")

d = f.read()
data = d.split()
for w in data:
    if not w.isnumeric():
        count+=1
        print(w)
print("No of Words :",count)