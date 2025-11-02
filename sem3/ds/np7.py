import numpy as np
arr=np.array([[1,2],[3,4]])
print(f"array:\n{arr}")
print(f"sum of all elements \n{np.sum(arr)}")
print("sum of column")
print(np.sum(arr,axis=0))
print("sum of row")
print(np.sum(arr,axis=1))