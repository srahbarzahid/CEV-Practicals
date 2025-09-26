import numpy as np

#arr = np.random.rand(4, 4)
arr = np.arange(1,17, dtype='int').reshape(-1,4)
print("original array")
print(arr)
arr = arr[[-1,1,2,0]]
print("after swapping\n",arr)