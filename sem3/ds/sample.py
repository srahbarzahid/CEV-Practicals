# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn import metrics
# import pandas as pd
#
# iris=load_iris()
# df=pd.DataFrame(iris.data,columns=iris.feature_names)
# df['target']=iris.target
# print(df.head())
#
# x=iris.data
# y=iris.target
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# knn=KNeighborsClassifier(n_neighbors=3)
# knn.fit(x_train,y_train)
# y_pred=knn.predict(x_test)
# print("prediction: ",y_pred)
# print(f"accuracy score:  {metrics.accuracy_score(y_test,y_pred)}")
# s=[[4,4,4,4]]
# pred=knn.predict(s)
# pred_v=[iris.target_names[p] for p in pred]
# print(f"prediction of [4,4,4,4]:  {pred_v}")
# print(f"confusion matrix:\n  {metrics.confusion_matrix(y_test,y_pred)}")

# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans
# import pandas as pd
#
# iris=load_iris()
# df=pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df.head())
#
# x=df.iloc[:, :4]
# print(x.head())
# km=KMeans(n_clusters=3)
# km.fit(x)
# y_pred=km.predict(x)
# print(f"prediction of clusters: {y_pred}")
# centroid=km.cluster_centers_
# print(f"centroid of clusters:  {centroid}")



# from sklearn.datasets import load_iris
# from sklearn.naive_bayes import GaussianNB
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, accuracy_score
# from sklearn.preprocessing import StandardScaler
# import pandas as pd
#
# iris=load_iris()
# df=pd.DataFrame(iris.data, columns=iris.feature_names)
# df['target']=iris.target
# print(df.head())
#
# X,y=load_iris(return_X_y=True)
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#
# sc=StandardScaler()
# sc.fit(X_train)
# X_train=sc.transform(X_train)
# X_test=sc.transform(X_test)
#
# gnb=GaussianNB()
# gnb.fit(X_train,y_train)
# y_pred=gnb.predict(X_test)
# print(f"prediction of guassian: {y_pred}")
# print(f"accuracy score:  {accuracy_score(y_test,y_pred)}")
# print(f"accuracy score: {gnb.score(X_test,y_test)}")
#
# s=[[5,5,4,4]]
# pred=gnb.predict(s)
# pred_v=[iris.target_names[p] for p in pred]
# print(f"prediction of [5,5,4,4] :   {pred_v}")
# print(f"confusion matrix:  {confusion_matrix(y_test,y_pred)}")


# from sklearn.datasets import load_diabetes
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score,mean_squared_error
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# data=load_diabetes()
# df=pd.DataFrame(data.data,columns=data.feature_names)
# print(df.head())
#
# x=df.iloc[:, 7]
# print(x.head())
#
# y=df.iloc[:, 6]
# print(y)
#
# x=np.array(x).reshape(-1,1)
# print("reshaped x: ",x)
# y=np.array(y).reshape(-1,1)
# print("reshaped y: ",y)
#
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
#
# lr=LinearRegression()
# lr.fit(x_train,y_train)
# y_pred=lr.predict(x_test)
# print("prediction of lr:  ",y_pred)
# print(f"r2 score:  {r2_score(y_test,y_pred)}")
# print(f"mean squared error:  {mean_squared_error(y_test,y_pred)}")
# print(f"coefficient : {lr.coef_}")
#
# plt.scatter(x_test,y_test,color='b', label="actual")
# plt.plot(x_test,y_pred,color='k',label="predicted")
# plt.xlabel("s5")
# plt.ylabel("s3")
# plt.title("linear regression")
# plt.legend()
# plt.show()



from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import pandas as pd

iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df['target']=iris.target
print(df.head())

X,y=load_iris(return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

sc=StandardScaler()
sc.fit(X_train)
X_train=sc.transform(X_train)
X_test=sc.transform(X_test)

gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)
print(y_pred)

print(f"accuracy score:  {metrics.accuracy_score(y_test,y_pred)}")
print(f"confusion matrix:  \n{metrics.confusion_matrix(y_test,y_pred)}")

s=[[4,4,4,4]]
pred=gnb.predict(s)
pred_v=[iris.target_names[p] for p in pred]
print(f"prediction of sample: {pred_v}")