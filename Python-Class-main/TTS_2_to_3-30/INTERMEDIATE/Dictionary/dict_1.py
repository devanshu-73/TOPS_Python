'''
    Dictionary : collection of key and pair elements

    Syntax : dict_name={key1:val1,key2:val2,..,keyn:valn}

    reresents with : {}
    in-built class : dict()

    characteristics :

    - dict in python are indexible (indexible by key)
    - keys have to be single valued  
    - they are mutable/unhashable/changable
    - they are unordered
    - they are iterable
    - value can be duplicate but keys are always unique
'''

# blank dicts

d1={}
d2=dict()

print(type(d1))
print(type(d2))

# diff dictionary declaration
dict_1={'k1':1,'k2':2}
dict_2={1:'key1',2:"HEllo",1.3:90}
dict_3={'k1':[12,43,5],'k2':67.34,'k3':"Hey"}

print(dict_1)
print(dict_2)
print(dict_3)















