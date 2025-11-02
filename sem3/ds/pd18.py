import pandas as pd
details={
    'name': ['d', 'g', 'b'],
    'age': [12, 21, 7]
}
df=pd.DataFrame(details)
print(df)
print()
print(df[:2])