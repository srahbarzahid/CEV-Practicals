import pandas as pd
data={
    'name':['a','b','c','d','e'],
    'occupation':['A1','A1','A1','B1','B1'],
    'salary':[1000,2000,1500,500,300]
}
df=pd.DataFrame(data)
print(df.to_string(index=False))
avg=df.groupby('occupation')['salary'].mean()
print(avg)