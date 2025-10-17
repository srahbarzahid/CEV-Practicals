import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Load diabetes dataset
data = datasets.load_diabetes()

# Convert to DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

# Append the target column
df['target'] = data.target

# Print first few rows
print(df.head())

# Use feature at column index 7 (s5) and target from column index 6 (s4) for demonstration
x = df.iloc[:, 7]  # s5
print("x (Feature - s5):")
print(x.head())
print()

y = df.iloc[:, 6]  # s4
print("y (Target - s4):")
print(y.head())
print()

# Reshape into 2D arrays
x = np.array(x).reshape(-1, 1)
print("Reshaped x:")
print(x)
print()

y = np.array(y).reshape(-1, 1)
print("Reshaped y:")
print(y)
print()

# Split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Create and train model
classifier = LinearRegression()
classifier.fit(x_train, y_train)

# Print model
print("Trained model:")
print(classifier)

# Predict
y_pred = classifier.predict(x_test)
print("Predicted values:")
print(y_pred)
print()

# Evaluate
print("R-squared score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Coefficients:", classifier.coef_)

# Plot results
plt.scatter(x_test, y_test, color='b', label='Actual')
plt.plot(x_test, y_pred, color='k', label='Predicted')
plt.xlabel('s5')
plt.ylabel('s4')
plt.title('Simple Linear Regression (s5 vs s4)')
plt.legend()
plt.savefig('regre.png')
