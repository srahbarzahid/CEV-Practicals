import pandas as pd
data1={
    'id':[1,2,3,4],
    'name':['a','b','c','d'],
    'stipend':[200,100,250,500]
}

data2={
    'id':[1,2,3,4],
    'designation':['aa','bb','cc','dd']
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)
print()

df=pd.merge(df1,df2,on='id')
print(df)