#memory
import numpy as np
a = [i for i in range(10000000)]
import sys
print(sys.getsizeof(a))

a = np.arange(10000000,dtype =np.int8)
print(sys.getsizeof(a))