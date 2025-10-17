from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
X,y=load_iris(return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=0)
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)
print(y_pred)
X_new=[[5,5,4,4]]
y_new=gnb.predict(X_new)
print(f"predicted output of [5,5,4,4]:   {y_new}")
print(f"naive bayes score:  {gnb.score(X_test,y_test)}")