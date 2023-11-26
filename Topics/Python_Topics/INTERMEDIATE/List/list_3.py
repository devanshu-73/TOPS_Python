'''
    List funciton

    max()
    min()
    sum()
    len()
    count()

    List methods     
        >>to add element
        1) list.append(element) : insert element at end of the list

        2) list.insert(pos,element) : insert element at specific position

        3) list.extend(element) : insert elements at end of list

        >>to remove element

        1) list.pop() : remove last element
            ilst.pop(index) : will remove from index

        2) list.remove(elemennt) : will remove based on element itself

        3) list.clear() : will blank the whole list

        ex: del keyword : remove specific element 
                    
'''
l1=[12,34,65,7,67,45]

print("Length before addition is : ",len(l1))

print(">>>>>>>>>>>>>>>>>Add elements : ")
l1.append(98)
print("Length after append is : ",len(l1))

print(l1)

l1.insert(3,[23,34,345,54])
print("Length after insert is : ",len(l1))
print(l1)

l1.extend([23,43,54,5])
print("Length after extend is : ",len(l1))
print(l1)
















