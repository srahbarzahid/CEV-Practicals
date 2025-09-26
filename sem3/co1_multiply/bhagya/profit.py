import pandas as pd
df=pd.DataFrame({
    'cname':['company A','company B','company C','company D'],
    'profit':[1000,-500,0,200]
})
df['profit']=df['profit']>0
print(df)