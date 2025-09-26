import numpy as np

a = np.array([2, 3, 5, 6, 5])
b = np.array([2, 3, 5, 6, 7])

array_equal = np.array_equal(a, b)

if array_equal:
    print("arrays are equal")
else:
    print("arrays are different")
