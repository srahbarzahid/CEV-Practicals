import pandas as pd
import numpy as np
data={'numbers':[2,3,np.nan,6,4,np.nan,7,np.nan,np.nan]}
df=pd.DataFrame(data)
print(df.to_string(index=False))
print()
df=df.fillna(0)
print(df.to_string(index=False))