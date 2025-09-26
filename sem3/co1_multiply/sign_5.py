import numpy as np

n = np.arange(21)
print("before changing the sign\n",n)
n[(n>=9) & (n<=18)] *= -1
#n *= -1
print("after changing sign\n",n)
