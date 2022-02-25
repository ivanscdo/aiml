import pandas as pd
import numpy as np

df8 = pd.DataFrame({'customer': ['101', '103', '104', '105'], 
                    'color': ['yellow', 'green', 'green', 'blue'], 
                    'distance': [12,9,44,21], 
                    'sales': [123,214,663,331]}, index=[4,5,6,7])

### DATAFRAME ATTRIBUTES
# print('df8')
# print(df8)

# print('.color')
# print(df8.color)

# print('.index')
# print(df8.index)

# print('.columns')
# print(df8.columns)

# print('.values')
# print(df8.values)

# print('.values[0,1')
# print(df8.values[0,1])

# print('.shape')
# print(df8.shape)

# print('.size')
# print(df8.size)

# print('.axes')
# print(df8.axes)

# print('.ndim') # number of dimensions
# print(df8.ndim)

# print("df8['color'].value_counts()")
# print(df8['color'].value_counts())

# print('.unique()')
# print(df8['color'].unique())


df9 = pd.DataFrame({'Q1': [101,102,103], 
                    'Q2': [201,202,204]}, 
                    index=['I0', 'I1', 'I2'])

# print(df9)
# print(df9.mean())
# print(df9.min())
# print(df9.max())

# print(df8.max())
# print(df8.sales.max())

# new_df = df8[(df8['customer'] != '105') & (df8['color'] != 'green')]
# new_df = df8[(df8['customer'] != '105')]
# new_df = df8[(df8['sales'] >= 215)]
# print(new_df)

def profit(s):
    return s*0.5

# print(df8.sales)
# print(df8.sales.apply(profit))
# print(df8['color'])
# print(df8['color'].apply(len))
# print()

# df8['profit'] = df8.sales.apply(profit)
# print(df8)

# print(df8.apply(profit))
# print(df8[['customer', 'distance', 'sales']])
df11 = df8[['distance', 'sales']]
# print(df11)
# print(df11.apply(profit))
# print(df11.applymap(profit))

# df11 = df8[['customer', 'distance', 'sales']] # throws type error; customer col is str!
# print(type(df8.customer[4]))
# print(type(df8.distance[4]))
# print(type(df8.sales[4]))
# for x in df8.sales:
#     print(x, type(x))

def col_sum(col):
    print(col)
    return sum(col)

# print(df11.apply(col_sum))
# print(df11.applymap(col_sum))


mydict = {'customer': ['Customer 1', 'Customer 1', 'Customer2', 'Customer2', 'Customer3', 'Customer3'], 
        'product1': [1.1,2.1,3.8,4.2,5.5,6.9], 
        'product2': [8.2,9.1,11.1,5.2,44.66,983]}
# print(mydict)
df6 = pd.DataFrame(mydict, index=['Purchase 1', 'Purchase 2', 'Purchase 3', 'Purchase 4', 'Purchase 5', 'Purchase 6'])
print(df6)

grouped_data = df6.groupby('customer')
print()
print(grouped_data.describe())