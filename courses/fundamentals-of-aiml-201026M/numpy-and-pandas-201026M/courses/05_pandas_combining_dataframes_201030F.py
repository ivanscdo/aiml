import pandas as pd
import numpy as np

### CONCAT
df7 = pd.DataFrame({"customer": ['101','102', '103', '104'], 
                    'category': ['cat2', 'cat2', 'cat1', 'cat3'], 
                    'sales': [123,52,214,663]}, index = [0,1,2,3])

df8 = pd.DataFrame({"customer": ['101', '103', '104', '105'], 
                    'color': ['yellow', 'green', 'green', 'blue'], 
                    'distance': [2,9,44,21], 
                    'sales': [123,214,663,331]}, index=[4,5,6,7])

# print(df7)
# print()
# print(df8)

# print()
# print(pd.concat([df7, df8],axis=0, sort=False))
# print()
# print(pd.concat([df7, df8],axis=0, sort=True))
# print()
# print(pd.concat([df7, df8], axis=1, sort=False))

### MERGE - combine on columns
# print(pd.merge(df7, df8, how='outer', on='customer'))# outer - union of all rows; all customers. 
# print(pd.merge(df7, df8, how='inner', on='customer')) # inner - intersection; only customers that exist in both. 
# print(pd.merge(df7, df8, how='left', on='customer')) # left - all customers in left side dataframe, df7 in this case. 
# print(pd.merge(df7, df8, how='right', on='customer')) # right - all customers in right side dataframe, df8 in this case. 

### JOIN - combine on index values
df9 = pd.DataFrame({'Q1': [101,102,103], 
                    'Q2': [201,202,204]},
                    index=['I0','I1','I2'])

df10 = pd.DataFrame({'Q3': [301,302,303], 
                    'Q4': [401,402,403]}, 
                    index=['I0', 'I2', 'I3'])

print('df9')
print(df9)
print('df10')
print(df10)
print('outer')
print(df9.join(df10,how='outer')) # outer - union; all rows.
print('inner')
print(df9.join(df10,how='inner')) # inner - rows in both DataFrames
print('left')
print(df9.join(df10,how='left')) # left - 
print('right')
print(df9.join(df10,how='right')) # right - 
