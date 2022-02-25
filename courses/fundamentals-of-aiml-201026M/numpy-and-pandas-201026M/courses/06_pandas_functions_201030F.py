import pandas as pd
import numpy as np

### PREDEFINED FUNCTIONS
df8 = pd.DataFrame({"customer": ['101', '103', '104', '105'], 
                    'color': ['yellow', 'green', 'green', 'blue'], 
                    'distance': [12,9,44,21], 
                    'sales': [123,214,663,331]}, index=[4,5,6,7])

# print('unique')
# print(df8['color'].unique())
# print('value_counts()')
# print(df8['color'].value_counts())

df9 = pd.DataFrame({'Q1': [101,102,103], 
                    'Q2': [201,202,204]},
                    index=['I0','I1','I2'])

# print(df9.mean())
# print(df8.columns)
print(df8)

# new_df = df8[(df8['customer'] != '105') & (df8['color'] != 'green')]
# print(new_df)

# print(df8['sales'].mean())
# print(df8['distance'].min())


### USER-DEFINED FUNCTION
def profit(s):
    return s*0.5

# print(df8['sales'])
# print(df8['sales'].apply(profit)) # apply allows use of user-defined function; outputs series
# print(df8['color'])
# print(df8['color'].apply(len))

df11 = df8[['distance', 'sales']]
# print(df11.applymap(profit)) #applymap - only works on dataframes, and onlu entry by entry

def col_sum(col):
    return sum(col)

# print(df11.apply(col_sum))
# print(df11.applymap(col_sum)) # only works on DataFrames

# print(df8)
# del df8['color']
# print(df8)

# print(df8.index)
print(df8.sort_values(by='distance')) # default desc
# print(df8.sort_values(by='distance', inplace=True)) # inplace sorts original dataframe

mydict = {'customer': ['Customer 1', 'Customer 1', 'Customer2', 'Customer2', 'Customer3', 'Customer3'], 
          'product1': [1.1,2.1,3.8,4.2,5.5,6.9], 
          'product2': [8.2,9.1,11.1,5.2,44.66,983]}
df6 = pd.DataFrame(mydict, index=['Purchse 1', 'Purchase 2', 'Purchase 3', 'Purchase 4', 'Purchase 5', 'Purchase 6'])
# print(df6)

grouped_data = df6.groupby('customer')
# print(grouped_data)

# print(grouped_data.describe())
# print(grouped_data.mean())
# print(grouped_data.std())
