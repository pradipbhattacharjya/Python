#Reshapin
import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)
# Transpose 
np.transpose(a2)
print(a2.T)

#ravel
print(a2.ravel())