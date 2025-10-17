import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
print("First few rows of the dataset:")
print(df.head())
print()
x = df.iloc[:, :4]
print(x.head())
print()
# Create KMeans model with 3 clusters
km = KMeans(n_clusters=3, random_state=42)
print("Fitting the model:")
print(km.fit(x))
print()
# Predict the cluster labels
y = km.predict(x)
print("Predicted cluster labels:")
print(y)
print()
# Get cluster centroids
centroid = km.cluster_centers_
print("Cluster centroids:")
print(centroid)
