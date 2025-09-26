import numpy as np

x = np.array([3,4,5,6])
y = np.array([5,6,3,6])
print("original arrays")
print(x)
print(y)

print("checking element wise")
#print(x==y)
print(np.equal(x,y))
print("checking the two arrays are equal or not")
print(np.array_equal(x,y))