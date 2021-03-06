import pandas as pd
import numpy as np

### 
df8 = pd.DataFrame({"customer": ['101', '103', '104', '105'], 
                    'color': ['yellow', 'green', 'green', 'blue'], 
                    'distance': [12,9,44,21], 
                    'sales': [123,214,663,331]}, index=[4,5,6,7])
del df8['color']
df8.sort_values(by='distance', inplace=True) # inplace sorts original dataframe
print(df8)

df8.to_csv('df8.csv', index=True) # 1st param is name; index=True - saves index labels as new column

new_df8 = pd.read_csv('df8.csv', index_col=0) # index_col is column to use as index
print(new_df8)

df8.to_excel('df8.xlsx', index=False,sheet_name='first_sheet') # name of file; save indexes?; name of tab/sheet
newer_df8 = pd.read_excel('df8.xlsx', sheet_name='first_sheet')
print(newer_df8)