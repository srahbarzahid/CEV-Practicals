import pandas as pd
data={'name':['a','b','c','d'],
      'age':[1,2,3,4]
      }
df=pd.DataFrame(data)
print(df[:2].to_string(index=False))