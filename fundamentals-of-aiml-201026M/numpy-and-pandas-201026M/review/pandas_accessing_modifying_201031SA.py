import pandas as pd
import numpy as np

### 03 PANDAS INTRO SERIES DATAFRAMES

mylist = [1,2,3,4]
myarray = np.array(mylist)

# print(mylist)
# print(myarray)

myseries1 = pd.Series(data=mylist)
myseries2 = pd.Series(data=myarray)

# print(myseries1)
# print(myseries2)

# for num in myseries1:
#     print(num)

# print(myseries1[0])
# print(myseries2[0])

mylabels = ['first', 'second', 'third', 'fourth']
myseries3 = pd.Series(data=mylist, index=mylabels)
myseries4 = pd.Series(mylist, mylabels)
# print(myseries3)

ex_series = pd.Series(data=[1,2,3,3], index=['one', 'two', 'three', 'four'])
# print(ex_series)
ex_series1 = pd.Series([1,2,3], ['one', 'two', 'three']) # shorthand
# print(ex_series1)

# print(ex_series1)
# print(ex_series1['one'])
myseries5 = pd.Series([5,1,5,7], ['first', 'third', 'fourth', 'fifth'])

df1 = pd.concat([myseries4, myseries5], axis=1, sort=False)
# print(df1)


df2 = pd.DataFrame(np.random.randn(5,5))

df3 = pd.DataFrame(np.random.randn(5,5), index=['first row', 'second row', 'third row', 'fourth row','fifth row'], columns=['first col', 'second col', 'third col', 'fourth col', 'fifth col'])
# print(df3)
# print()

### 04 PANDAS ACCESSING AND MODIFYING
# print(df3['second col'])
# print(df3[['second col', 'third col']])

# print()
# print(df3.loc['fourth row'])

# ex_series2 = pd.Series(df3.loc['fourth row'])
# print(ex_series2)

# print(df3.iloc[3])
# print(df3.loc[['fourth row', 'first row'], ['second col','third col']])

df3['sixth col'] = np.random.randn(5,1)
# print(df3)
# print(df3.drop('first col', axis=True, inplace=True))
# print(df3)

df5 = df3.drop('second row', axis=0)
# print(df5)

# print(df5.reset_index(inplace=True))

df5['new name'] = ['this', 'is', 'the', 'row']
# print(df5)
# df5.loc[5] = ['red', 'wine', ',', 'success', '!', 'x', 'x']

# print(df5.shape[0])
# print(len(df5.columns))
# print(len(df5.index))

# print(df5)
# for x in df5:
#     print(x)

# df5.set_index('new name', inplace=True)
# print(df5)

