import numpy as np
x = np.array([3,4,5,1])
y = np.array([2,3,6,1])

print("first array\n",x)
print("second array\n",y)

print("A>B")
print(np.greater(x,y))

print("A>=B")
print(np.greater_equal(x,y))

print("A<B")
print(np.less(x,y))
