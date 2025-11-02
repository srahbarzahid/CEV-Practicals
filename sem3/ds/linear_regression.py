from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=load_diabetes()
df=pd.DataFrame(data.data, columns=data.feature_names)
df['target']=data.target
print(df.head())

x=df.iloc[:, 7]
print("x feature s5")
print(x.head())

y=df.iloc[:, 6]
print("x feature s3")
print(y.head())
x=np.array(x).reshape(-1,1)
print(f"reshaped x: \n {x}")
y=np.array(y).reshape(-1,1)
print(f"reshaped y: {y}")

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
print(y_pred)

print(f"r2 score:  {r2_score(y_test,y_pred)}")
print(f"mean square error:  {mean_squared_error(y_test,y_pred)}")
print(f"coefficient:  {lr.coef_}")

plt.scatter(x_test,y_test,color='b',label="Actual")
plt.plot(x_test,y_pred,color='k',label='Predicted')
plt.xlabel('s5')
plt.ylabel('s3')
plt.title('linear regression')
plt.legend()
plt.show()