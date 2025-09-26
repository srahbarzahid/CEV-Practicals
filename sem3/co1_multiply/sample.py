import matplotlib.pyplot as plt

import numpy as np
x= np.array([1,2,6,18])
y = np.array([4,16,13,22])

plt.plot(x, y, marker = 'o', mec = 'r')
plt.savefig('image.png')