import pandas as pd

# Generate the date range
date_series = pd.date_range(start='2021-5-1', end='2021-5-12')

# Print the result
print("Date series from 1st may 2021 to 12th may 2021:")
print(date_series)
