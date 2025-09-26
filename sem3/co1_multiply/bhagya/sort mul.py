import pandas as pd
data = {
    'Name':['Alice','Bob','Charlie','Bob','Alice'],
    'Age':[25,30,22,25,30],
    'Score':[85,90,95,88,82]

}
df=pd.DataFrame(data)
sorted_df=df.sort_values(by=['Name','Age'],ascending=[True,False])
print(sorted_df)