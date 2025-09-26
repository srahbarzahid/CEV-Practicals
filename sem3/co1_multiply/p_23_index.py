import pandas as pd
data={
    'name':['e','a','a','b','c','d'],
    'age':[20,1,2,3,45,5],
    'rank':[0,1,2,3,4,5]
}
index = ['a1','b1','c1','d1','e1','f1']
df=pd.DataFrame(data,index)
print(df.to_string())
df.reset_index(inplace=True)
print(df.to_string())