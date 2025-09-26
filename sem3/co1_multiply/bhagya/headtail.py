import pandas as pd

# Create a dictionary
data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Score': [85, 90, 95, 88, 76, 92]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the full DataFrame
print("Full DataFrame:")
print(df)

# Display the head (first 5 rows)
print("\nHead of the DataFrame:")
print(df.head())

# Display the tail (last 5 rows)
print("\nTail of the DataFrame:")
print(df.tail())
