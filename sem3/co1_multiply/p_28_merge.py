import pandas as pd
d1={
    'eid' : [1,2,3,4],
    'ename' : ['a','b','c','d'],
    'stipend':[123,131,23,434],
}
d2={
    'eid' : [1,2,3,4],
    'designation' : ['aa','bb','cc','dd'],
}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
df=pd.merge(df1,df2,on='eid')
print(df)