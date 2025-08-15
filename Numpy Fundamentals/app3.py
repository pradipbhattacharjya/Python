#Array Operations
import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a1)
#arithmetic
print(a1 **2)

#relational
print(a2 > 25)

#vector operations
#arithmetic
print(a1 + a2)