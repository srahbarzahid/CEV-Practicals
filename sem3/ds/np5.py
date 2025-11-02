import numpy as np
x=np.arange(21)
print("array:\n",x)
x[(x>=9) & (x<16)]*=-1
print("updated:\n",x)