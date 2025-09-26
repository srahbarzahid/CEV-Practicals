import numpy as np
import matplotlib.pyplot as plt

x = np.array([12,14,16,18,20,22,24])
y = np.array([100,200,250,400,300,450,500])

plt.plot(x, y, marker = 'o', mfc='g', c='r', linestyle = 'dashed',mec='g')
plt.savefig('p12.png')
