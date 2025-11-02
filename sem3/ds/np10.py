import numpy as np
arr=np.arange(16,dtype='int').reshape(-1,4)
print(f"array:\n{arr}")
narr=arr[[-1,1,2,0]]
print("after swapping")
print(narr)