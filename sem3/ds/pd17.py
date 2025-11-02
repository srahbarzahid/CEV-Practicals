import pandas as pd
details={
    'name':['a','b','c','d'],
    'age':[21,23,12,14],
    'rank':[2,21,14,1]
}
index=['i1','i2','i3','i4']
df=pd.DataFrame(details,index)
print(df)
df_n=df.reset_index(drop=True)
print(df_n)