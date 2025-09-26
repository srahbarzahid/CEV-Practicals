import matplotlib.pyplot as plt

x=['java','python','php','javascript','c#','c++']
y=[22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(x, y, color='skyblue')
plt.xlabel("programming languages")
plt.ylabel("popularity %")
plt.title("popularity of programming Languages")
plt.savefig('p_16_2.png')