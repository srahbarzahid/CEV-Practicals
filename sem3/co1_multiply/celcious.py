import matplotlib.pyplot as plt
import numpy as np
temp=np.array([12,14,16,18,20,22,24])
celcious=np.array([100,20,250,400,300,450,500])
plt.plot(temp,celcious,marker='o',linestyle='-',color='violet',mec='cyan',mfc='b')
plt.savefig('celcious.png')