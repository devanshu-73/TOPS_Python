str1="Hello all welcome. I have 5 books"

print("index element : ",str1[6])
print("index element : ",str1[-1])

# string slicing
# use slice ':'
# eg : str_name[start:stop]  (stop excluded)

print("slicing : ",str1[10:17])

# strings are iterable
for i in str1:
    print(i)
