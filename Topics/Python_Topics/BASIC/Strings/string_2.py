str1=input("Enter any string : ")
ch=input("Enter any character : ")

ch_freq=0
for i in str1:
    if ch==i:
        ch_freq+=1

print(ch_freq)
