my_set = {1,2,3,4,5,5,5,5,5,5}
print(my_set)

print(type(my_set))


a = {1,2,3,4,5,5,5,5,5}
b = {10,11,3,2,5}

print(a.union(b))
print(a.intersection(b))

a.remove(2)
print(a)

a.add(20)
print(a)