import pandas as pd

date=pd.date_range('2021-05-01','2021-05-12',freq='D')
x = pd.Series(date)
print(x.to_string(index=False))