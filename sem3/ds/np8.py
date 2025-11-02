import numpy as np
x=np.arange(16).reshape(4,4)
header="C1 C2 C3 C4"
np.savetxt('arr.txt',x,fmt="%d",header=header)
print("after loading the text file")
print(np.loadtxt('arr.txt'))