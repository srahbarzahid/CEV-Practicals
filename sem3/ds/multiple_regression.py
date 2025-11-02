from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
y_pred_train=lr.predict(x_train)
print(y_pred)
print(y_pred_train)
print(f"r2 score:  {r2_score(y_test,y_pred)}")
print(f"mean square error:  {mean_squared_error(y_test,y_pred)}")