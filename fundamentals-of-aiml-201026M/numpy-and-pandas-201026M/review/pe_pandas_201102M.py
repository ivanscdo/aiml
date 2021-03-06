import numpy as np
import pandas as pd

# series2 = pd.Series(data = [1,2,3], index = ['key1', 'key2', 'key3'])
# print(series2)

# mydict = {'red':6, 'wine':8, 'succes':10}
# print(mydict)
# series3 = pd.Series(mydict)
# print(series3)

# print(np.dot(series2, series3))

# d1 = {'a': [1,2,3], 'b': [3,4,5], 'c':[6,7,8] }
# # df1 = pd.DataFrame(d1, index=['x', 'y', 'z'])
# df1 = pd.DataFrame(d1)
# print(df1)
# print(df1.iloc[1])
# print(df1.iloc[1, 2])
# print(df1.loc[1, 'c'])


mtcars = pd.read_csv('../practice-exercises/mtcars.csv')
mtcars.index = mtcars['name']
# print(mtcars.drop('name', axis=1))
# print(mtcars.shape)
# print(type(mtcars))

# mtcars_tp = [type(x) for x in mtcars]
# print(mtcars_tp)

# for item in mtcars.iteritems():
#     print(item)

mtcars.head(10)
mtcars.tail(10)

# print(mtcars.columns)

# print(mtcars.iloc[:6,:3])
print(mtcars.loc['Mazda RX4':'Valiant', 'mpg':'cyl'])
print(mtcars.sort_values(by='mpg'))