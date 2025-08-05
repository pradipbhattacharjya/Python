#Operations on Lists

#Arithmetic
L1 = [1,2,3,4]
L2 = [5,6,7,8]
#Concatenation/Merge
print(L1 + L2)
print(L1 *3)

#Membership
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
print(5 in L1)
print(5 in L2)
print([5,6] in L2)

#Loop
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

for i in L2:
    print(i)

L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

for i in L3:
    print(i)