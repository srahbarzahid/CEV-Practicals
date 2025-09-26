import matplotlib.pyplot as plt

with open('data_13.txt') as f:
    data = f.read()
data = data.split('\n')
x = [int(row.split(' ')[0]) for row in data]
y = [int(row.split(' ')[1]) for row in data]
plt.plot(x,y, marker='o', mfc='r', mec='r')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("graph")
plt.savefig('p13.png')