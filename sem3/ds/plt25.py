import matplotlib.pyplot as plt
with open('data.txt') as f:
    data=f.read()
data=data.split('\n')
x=[int(row.split(" ")[0]) for row in data]
y=[int(row.split(" ")[1]) for row in data]
plt.plot(x,y,marker='o',mec='g',mfc='g')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()