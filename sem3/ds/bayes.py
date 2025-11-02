import pandas as pd
from sklearn.datasets import load_iris
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
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
print(f"prediction of testing values: \n {y_pred}")

X_new=[[5,5,4,4]]
y_new=gnb.predict(X_new)
print(f"predicted output of [5,5,4,4]:   {y_new}")
y_name=[iris.target_names[p] for p in y_new]
print(y_name)
print(f"naive bayes score:  {gnb.score(X_test,y_test)}")
print(f"confusion matrix:\n  {metrics.confusion_matrix(y_test,y_pred)}")