import pandas as pd
from sklearn.cluster import KMeans
data = pd.real_csv('iris.csv')
print("First few rows of the dataset:")
print(data.head())
print()
x = data.iloc[:, :4]
print(x.head())
print()
km = KMeans(k_cluster=3)
print(km.fit(x))
print()
y = km.predict(x)
print(y)
print(x)