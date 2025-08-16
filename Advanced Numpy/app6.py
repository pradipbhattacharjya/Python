#Plotting Graphs
import numpy as np
import matplotlib.pyplot as plt
#plotting a 2D plot
#x = y

x = np.linspace(-10,10,100)
print(x)
y = x
# print(y)

print(plt.plot(x,y))

# y = x^2

x = np.linspace(-10,10,100)
y = x ** 2

print(plt.plot(x,y))

# y = sin(x)
x = np.linspace(-10,10,100)
y = np.sin(x)

print(plt.plot(x,y))

# y = xlog(x)
x = np.linspace(-10,10,100)
y = x *np.log(x)
print(x,y)

# sigmoid
x = np.linspace(-10,10,100)
y = 1/(1+np.exp(-x))

print(plt.plot(x,y))