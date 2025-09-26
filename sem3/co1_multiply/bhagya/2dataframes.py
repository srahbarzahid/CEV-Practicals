import pandas as pd
df1=pd.DataFrame({
    'eid':[101,102,103],
    'ename':['Alice','Bob','Charlie'],
    'stipend':[5000,6000,5500]
})
df2=pd.DataFrame({
    'eid':[101,102,103],
    'designation':['manager','developer','analyst']

})
result_df=pd.merge(df1,df2,on='eid')
result_df.rename(columns={'designation':'position'},inplace=True)
print(result_df)