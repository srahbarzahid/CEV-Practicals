import pandas as pd
df = pd.read_csv('p21.csv')
print(df.to_string(index=False))