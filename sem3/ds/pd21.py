import pandas as pd
data={
    'cname':['a','b','c','d'],
    'profit':[21,-20,10,0]
}
df=pd.DataFrame(data)
print(df)
print()

df['profit']=df['profit']>0
print(df.to_string(index=False))