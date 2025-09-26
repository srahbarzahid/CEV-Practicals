import numpy as np

x = np.arange(16)

print("Array:")
print(x)

header = 'array'
np.savetxt('array.txt', x, fmt="%d", header=header)

print("\nAfter loading")
print(np.loadtxt('array.txt'))