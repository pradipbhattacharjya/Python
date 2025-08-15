#Stacking
import numpy as np
# horizontal stacking
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)
a5
print(np.hstack(a4,a5,a4))
# Vertical stacking
print(np.vstack((a4,a5)))