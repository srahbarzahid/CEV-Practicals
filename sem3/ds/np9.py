import numpy as np
a1=np.array([1,3,4,5])
a2=np.array([2,4,4,5])
print(f"array1\n{a1}")
print(f"array2:\n{a2}")
print("equal or not")
res1=np.equal(a1,a2)
print(res1)
res=a1==a2
print(res)