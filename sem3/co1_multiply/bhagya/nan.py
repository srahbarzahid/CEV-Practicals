import pandas as pd
import numpy as np
df=pd.DataFrame({
    'name':['Alice','Bob','Charlie','David'],
    'occupation':['Engineer','Doctor',np.nan,'Doctor'],
    'salary':[70000,120000,np.nan,110000]

})
df_filled=df.fillna(0)
print(df_filled)