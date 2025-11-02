import pandas as pd
date=pd.Series(pd.date_range('2021-05-01','2021-05-13'))
print(date.to_string(index=False))