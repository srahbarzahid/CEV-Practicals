import pandas as pd
details={
    'name':['d','g','b'],
    'age':[12,21,7],
    'rank':[2,12,1]
}
df=pd.DataFrame(details)
print(df)
dfs=df.sort_values(by=['name','age'], ascending=[True,True])
print(dfs)