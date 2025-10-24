from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
import pandas as pd

iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
df['target']=iris.target
print(df.head())

x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

svm=SVC(kernel='linear')
svm.fit(x_train,y_train)
y_pred=svm.predict(x_test)
print(f"prediction of testing datas:  {y_pred}")

print(f"accuracy score: {metrics.accuracy_score(y_test,y_pred)}")
sample=[[4,4,5,5]]
pred=svm.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(f"prediction of sample value [4,4,5,5]:  {pred_v}")
print()
print(f"confusion metrics:\n  {metrics.confusion_matrix(y_test,y_pred)}")