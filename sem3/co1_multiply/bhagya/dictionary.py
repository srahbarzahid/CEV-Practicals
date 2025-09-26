import pandas as pd

# Create a dictionary
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 95]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Converted DataFrame from dictionary:")
print(df)