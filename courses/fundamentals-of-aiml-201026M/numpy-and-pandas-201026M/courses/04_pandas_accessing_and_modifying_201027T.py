import pandas as pd
import numpy as np

### ACCESSING COLUMNS IN DATAFRAME
df3 = pd.DataFrame(np.random.randn(5,5), index=['first row', 'second row', 'third row', 'fourth row', 'fifth row'], columns = ['first col', 'second col', 'third col', 'fourth col', 'fifth col'])
# print(df3)
# print(df3['second col'])
# print(df3[['third col', 'first col']])

### ACCESSING ROWS IN DATAFRAME WITH STRING
# print(df3.loc['fourth row']) # turns dataframe row into series

### ACCESSING ROWS IN DATAFRAME WITH INDEX INT
# print(df3.iloc[2]) 

### ACCESSING ROW AND COLUMN IN DATAFRAME
# print(df3.loc[['fourth row', 'first row'],['second col', 'third col']])

### LOGICAL INDEXING
# print(df3>0) # returns dataframe True or False
# print(df3[df3>0]) # returns dataframe value for True values and NaN for False values

### CREATE NEW COLUMN
df3['sixth col'] = np.random.randn(5,1) # upserts; if exists updates, if not creates
# print(df3)

### REMOVE COLUMNS OR ROWS
# print(df3.drop('first col', axis=1)) # axis=1 to drop column, 0 to drop row; .drop func returns new dataframe, does not modify existing dataframe
# print(df3)

df4 = df3.drop('first col', axis=1)
# print(df4)

df5 = df3.drop('second row',axis=0)
# print(df5)

### REMOVE STRING LABELS
# print(df5.reset_index()) # function that returns, does not modify
print(df5.reset_index(inplace=True)) # passing inplace arg, saves output of .reset_index() func into existing dataframe; can also be used for .drop()

### MODIFY NAME OF INDEX
df5['new name'] = ['this', 'is', 'the', 'row']
print(df5)

df5.set_index('new name', inplace=True)
print(df5)

