#changing Datatype
import numpy as np

a1 = np.arange(10)
a2 = np.arange(12,dtype= float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
#astype
print(a3.astype(np.int32))
