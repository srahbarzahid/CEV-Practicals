import matplotlib.pyplot as plt
import numpy as np

x=np.array([12,14,16,18,20,22,24])
y=np.array([100,200,250,400,300,450,500])
plt.plot(x,y,marker='o',mec='g',mfc='g',linestyle='dashed')
plt.show()