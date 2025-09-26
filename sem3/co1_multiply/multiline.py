import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

x1=[1,2,3,4,5]
y1=[2,3,5,7,11]
x2=[1,2,3,4,5]
y2=[1,4,6,8,10]
plt.plot(x1,y1,label='Line 1',marker='o',linestyle='--',color='b')
plt.plot(x2,y2,label='Line 2',marker='x',linestyle='-',color='cyan')
plt.title('Two Lines On Same Plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(True)
plt.savefig('multiline.png')