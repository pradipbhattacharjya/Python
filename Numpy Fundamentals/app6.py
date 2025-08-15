#iterating
import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

# 1D
for i in a1:
    print(i)

#2D
for i in a2:
    print(i)


#3D
for i in a3:
    print(i)


for i in np.nditer(a3):
    print(i)