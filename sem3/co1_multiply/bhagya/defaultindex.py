import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],'Age':[25,30,35]
}
custom_index=['a','b','c']
df=pd.DataFrame(data,index=custom_index)
print("original dataframe with custom index:")
print(df)
df_reset=df.reset_index(drop=True)
print("\nDataframe with default integer index :")
print(df_reset)