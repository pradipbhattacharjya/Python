# Splitting
import numpy as np
# horizontal stacking
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)
a5
print(np.hsplit(a4,2))
# vertical splitting
print(np.vsplit(a5,3))