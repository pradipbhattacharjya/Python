#isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}

print(s1.isdisjoint(s2))


s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issubset(s2))

# copy 
s1 = {1,2,3}
s2 = s1.copy()

print(s1)
print(s2)

