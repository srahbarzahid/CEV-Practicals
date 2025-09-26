import matplotlib.pyplot as plt

x=['java','python','php','javascript','c#','c++']
y=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["yellow","red","maroon","green","black","cyan"]
fig = plt.figure(figsize=(10,6))
plt.bar(x, y, color=colors)
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("popularity of programming Languages")
plt.savefig('p_16_3.png')