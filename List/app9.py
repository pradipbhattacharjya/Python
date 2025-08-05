#List Functions
#len/min/max/sorted
L = [2,1,5,7,0]

print(len(L))
print(min(L))
print(max(L))
print(sorted(L))
print(sorted(L,reverse=True))

#count
L = [1,2,1,2,3,1,5]
print(L.count(1))
print(L.count(15))

#index
L = [1,2,1,2,3,1,5]
print(L.index(1))

#reverse
L = [2,1,5,7,0]
# permanently reverses the list
print(L.reverse())
print(L)

#sort (vs sorted)
L = [2,1,5,7,0]
print(L)
print(sorted(L))
print(L)
L.sort()
print(L)

#copy - Shallow
L = [2,1,5,6,0]
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))


