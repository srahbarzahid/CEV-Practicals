import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(popularity, labels=languages)

# Title
plt.title('Popularity of Programming Languages')

# Display the chart
plt.axis('equal')  # Ensures the pie chart is circular
plt.savefig('p_16_4')
