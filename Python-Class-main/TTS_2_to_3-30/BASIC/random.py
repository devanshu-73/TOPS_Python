import random

l1=[12,43,56.45,"hello",34,'R']

num = random.randint(1,100)

print(num)

element=random.choice(l1)
print(element)

#random.shuffle() : randomized the collection (in place change)

random.shuffle(l1)

print(l1)


