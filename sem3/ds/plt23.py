import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,marker='o',mec='g',mfc='g',c='r',linestyle='dotted')
plt.show()