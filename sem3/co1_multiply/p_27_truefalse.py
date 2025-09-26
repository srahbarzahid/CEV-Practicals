import pandas as pd
data={
    'cname':['a','b','c','d'],
    'profit':[24,56,0,-21]
}
df=pd.DataFrame(data)
print(df)
df.loc[df.profit>0,'profit']=True
df.loc[df.profit<=0,'profit']=False
print(df)