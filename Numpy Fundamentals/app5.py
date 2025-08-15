# Indexing and Slicing
import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print(a3)
#Indexing
print(a1)
print(a1[-1])
# 2D
print(a2[1,2])
print(a2[2,3])
print(a2[1,0])

# 3d

print(a3[1,0,1])
print(a3[0,1,0])
print(a3[0,0,0])
print(a3[1,1,0])

# Slicing
# 1D
print(a1[2:5])

#2D
print(a2[0,:])
print(a2[:,2])
print(a2[1:,1:3])
print(a2[::2,::3])
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[0:2,1:])

#3D
print(a3)
print(a3[0,1,:])
print(a3[1,:,1])
print(a3[2,1:,1:])
print(a3[::2,0,::2])
