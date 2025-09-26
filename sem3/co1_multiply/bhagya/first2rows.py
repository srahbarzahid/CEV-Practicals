import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],'Age':[25,30,35]
}
custom_index=['a','b','c']
df=pd.DataFrame(data,index=custom_index)
print("original dataframe with custom index:")
print(df)
first_two_rows=df.head(2)
print("first two rows of the table :")
print(first_two_rows)