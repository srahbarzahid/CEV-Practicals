import matplotlib.pyplot as plt

figure, axis = plt.subplots(2,2)


x1 = [10,20,30]
y1 = [10,20,30]
axis[0,0].plot(x1, y1)
axis[0,0].set_title("Plot 1")

x2 = [10,20,30]
y2 = [3,10,4]
axis[0,1].plot(x2, y2)
axis[0,1].set_title("Plot 2")

x3 = [20,40,60]
y3 = [5,14,18]
axis[1,0].plot(x3,y3)
axis[1,0].set_title("plot 3")

x4 = [12,14,16]
y4 = [4,6,7]
axis[1,1].plot(x4,y4)
axis[1,1].set_title("plot 4")
plt.savefig('p15.png')