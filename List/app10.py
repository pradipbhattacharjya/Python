#List Comprehension
# Add 1 to 10 numbers to a list
L =[]

for i in range(1,11):
 L.append(i)
print(L)

L = [i for i in range(1,11)]
print(L)