import numpy as np

x = np.array([[1,2,3],[3,4,1]])
print(x)
print("sum of all elements")
print(np.sum(x))

print("sum of each column")
print(np.sum(x, axis=0))

print("sum of each row")
print(np.sum(x, axis=1))