import pandas as pd
df=pd.DataFrame({
    'name':['Alice','Bob','Charlie','David'],
    'occupation':['Engineer','Doctor','Engineer','Doctor'],
    'salary':[70000,120000,80000,110000]

})
average_salary=df.groupby('occupation')['salary'].mean().reset_index()
print(average_salary)