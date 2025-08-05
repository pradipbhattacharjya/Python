#Deleting items from a List
L = [1,2,3,4,5]
print(L)
#del
del L[-1]
print(L)
#slicing
del L[1:3]
print(L)
#remove
L = [1,2,3,4,5]
L.remove(5)
print(L)

#pop
L = [1,2,3,4,5]
L.pop(0)
L.pop()
print(L)

#clear
L = [1,2,3,4,5]
L.clear()
print(L)