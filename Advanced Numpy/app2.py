# Advanced Indexing
import numpy as np
# Normal Indexing and slicing

a = np.arange(24).reshape(6,4)
# print(a)
# print(a[::2])
# Fancy Indexing
# print(a[:,[0,2,3]])

#Boolean Indexing
a = np.random.randint(1,100,24).reshape(6,4)
print(a)
#find all numbers greater than 50
print(a>50)
print(a[a > 50])


# find out  even number
print(a[a % 2 == 0])

#find all number greater than 50 and are even
print((a > 50) & (a % 2 == 0))
print(a[(a > 50) & (a % 2 == 0)])

#find all numbers not divisible by 7
print(a[~(a % 7 == 0)])