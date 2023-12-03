# random module

import random


l1=[12,23,54,6,7]

# generate random number from given range of integers
num=random.randint(1,100)

# generate random element from collection
var=random.choice(l1)

# will shuffle all the elements in place
random.shuffle(l1)

print("Shuffled list : ",l1)
print("random from list : ",var)

print("arndom from 1 to 100 : ",num)
