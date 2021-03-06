import numpy as np
import pandas as pd

# # py_1 = [i for i in range(10000)]
# # len(py_1

# # %%timeit #what is this?? benchmarking function only on jypiterlab
# # global py_1
# # py_1 = [i*2 for i in py_1]

# # arr - np.array([i for i in range(10000)])
# # %%timeit
# # global arr
# # arr *= 2

# l1 = [1,2,3,4]
# l2 = [4,1,3,2]

# # print(l2[0])

# l1 ==l2

# l1[0]

# l3 = [21.42, 'foobar', 3, 4, 'bark', False]
# # print(l3)

# dict = {1: 'apple', 2:'pear', 3:'lemon'}
# # print(dict)

# # print(dict.keys())

# # print(dict.values())

# v = dict.values()
# # v[0]
# v1 = list(v)
# print(v1[0]) 
# # can typecast!


df = pd.read_csv('uberdrive.csv')
# print(df.head(3))
# print(df.tail(3))

# print(df.shape)
# print(df.size)

# print(df.describe())

# df.MILES*.max # will remove star in column name!

# print(list(df.columns))

# print(df.info()) # check sanity of data; see what is missing, etc. 

# print(df.isnull())

# print(df.isnull().any()) # any refers to column perspective; any missing value

# print(df.isnull().sum())

# print(df[df['PURPOSE*'].isnull()].head(10)) # retrieve 10 rows, where purpose is null

# dataframe['column_name'] - retrieves series
# dataframe.column_name - retrieves column

# print(df['PURPOSE*'].count())

# print(df[df['END_DATE*'].isnull()])

# df.drop(1155, inplace = True)
# difference between shallow copy and deep copy

# print(df.shape)

# option 1 for replacing colymns
# new_names = ["Start_DATE", 'END_DATE', 'CATEGORY', 'START', 'STOP', 'MILES', 'PURPOSE']

# df.columns = new_names

# option 2
df.columns  = df.columns.str.replace('*', '')

# if only 1 column to replace
# df.rename(columns = {'CATEGORY': 'CATEGORY*'})
# print(df.head())

data = df[df.PURPOSE.isnull()]

# print(data)

data2 = df[~df.PURPOSE.isnull()] # negate 

# print(data2)

### DROP ROWS THAT HAVE NULL VALUES

df_dropped = df.dropna() # remove all nulls

# print(df_dropped.shape)

# .shape is attribute, not method!!

# print(df['MILES'].mean())
# print(df)

# df[(df['MILES'] == 10)]
# print(df[(df['PURPOSE'] == 'Meeting')])

# SQL WAY
df.query("MILES > 10")

# MULTIPLE CONDITIONS
df[(df['MILES'] > 200) & (df["PURPOSE"] == "Meeting")]

df[(df.MILES > 30) & (df.PURPOSE == "Meeting")]

df.shape

df.MILES.max()

df.MILES

df.MILES = df.MILES.max()

df[df.MILES == df.MILES.max()]

# print(df['START'].unique())
# print(len(df['START'].unique()))
# print(df['START'].nunique()) # number of unique 

df['START'].value_counts().head(10)

df[df['START'] == df['STOP']].head(5)


# start_dis = df.group('START')['MILES'].sum().sort_values(ascending = False)
start_dis = df.groupby('START')['MILES'].mean().sort_values(ascending = False)
print(start_dis)
type(start_dis)

start_dis = start_dis.reset_index()
type(start_dis)
start_dis.columns = ['Start', 'Miles']

# ...


# change datetime 

# mentor homework: 
# 1. difference btw dictionary and list. what are their pros and cons?
# 2.what's the difference btw shallow copy and deep copy
# 3. what's the difference btw map and apply
# 4. What's the different of iloc and loc

