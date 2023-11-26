# dicts are iterable

#dict method: dict.keys(), dict.values(), dict.items()

d1={
    'k1':1,
    'k2':2,
    'k3':3
    }


for i in d1.items():
    print(i)
    print(type(i))

print(">>>>>>>>>>>>>>>>>>>>>")
for k,v in d1.items():
    print(f'{k} = {v}')
