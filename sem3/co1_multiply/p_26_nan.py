import pandas as pd
import numpy as np
data={'numbers':[1,2,4,6,5,np.nan,8,23,np.nan,23,4,9,np.nan]}
df=pd.DataFrame(data)
print(df)
df_fill=df.fillna(0)
print(df_fill.to_string(index=False))