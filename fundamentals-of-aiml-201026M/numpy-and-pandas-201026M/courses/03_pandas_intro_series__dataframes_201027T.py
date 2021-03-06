# pandas - package for managing data
# 2 new data types: series & dataframe
# dataframe is similar to spreadsheet, with rows & columns
# series is a column in a dataframe
# can convert subset of dataframe into numpy array
# has sql-like functions for merging, joining, sorting

import pandas as pd
import numpy as np

### CREATE LIST AND CREATE ARRAY FROM LIST
mylist = [5.4,6.1,1.7,99.8]
myarray = np.array(mylist)
# print(mylist)
# print(myarray)

### CREATE SERIES FROM LIST AND ARRAY
myseries1 = pd.Series(data=mylist)
# print(myseries1)
myseries2 = pd.Series(data=myarray)
# print(myseries2)

### ACCESS VALUE IN SERIES
# print(myseries1[2])

### CREATE STRING INDEX FOR SERIES
mylabels = ['first', 'second', 'third', 'fourth']
myseries3 = pd.Series(data=mylist,index=mylabels)
# print(myseries3)

### CREATE SERIES AND INDEX, SHORTHAND
myseries4 = pd.Series(mylist,mylabels)
# print(myseries4)

### ACCESS VALUE IN SERIES WITH STRING
# print(myseries4['second'])

### ADD VALUES IN TWO SERIES
myseries5 = pd.Series([5.5,1.1,8.8,1.6],['first', 'third', 'fourth', 'fifth'])
# print(myseries5)
# print()
# print(myseries4)
# print()
# print(myseries5+myseries4) # will return NaN on indexes that don't match; index names must be the same in both series

### CREATE A DATAFRAME WITH .CONCAT()
df1 = pd.concat([myseries4, myseries5], axis=1, sort=False) # axis - columns in dataframe; does not sort indexes alphabetically
# print(df1)

### CREATE A DATAFRAME WITH .DATAFRAME() 
df2 = pd.DataFrame(np.random.randn(5,5))
# print(df2)

df3 = pd.DataFrame(np.random.randn(5,5), index=['first row', 'second row', 'third row', 'fourth row', 'fifth row'], columns = ['first col', 'second col', 'third col', 'fourth col', 'fifth col'])
# print(df3)