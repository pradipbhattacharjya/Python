#Working with mathematical formulas
import numpy as np
a = np.arange(10)
print(a)
print(np.sum(a))
print(np.sin(a))


# sigmoid 
def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

a = np.arange(100)
print(sigmoid(a))

#mean squared error
actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
   return np.mean(actual - predicted)**2

print(actual,predicted)

# categorical cross entropy
print(np.mean((actual - predicted)**2))