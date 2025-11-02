import pandas as pd
details={
    'name':['a','b','c','d'],
    'occupation':['a1','a2','a1','a2'],
    'salary':[1000,2300,1400,5000]
}
df=pd.DataFrame(details)
print(df)
avg=df.groupby('occupation')['salary'].mean()
print(avg)