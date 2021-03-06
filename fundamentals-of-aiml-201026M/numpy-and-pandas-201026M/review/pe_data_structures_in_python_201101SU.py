import numpy as np
import pandas as pd

### PE_Data_structures_in_Python
# l3 = [2,4,6,8]
# # print(l3)

# # arrl3 = np.array(l3)

# # # print(arrl3.append([0,1,3,3,5,5,7,9]))
# # arrl3.append((0,1,3,3,5,5,7,9))
# # print(arrl3)
# # print(l3.count(5))

# l3_cp = l3+[0,1,3,3,5,5,7,9]
# # print(l3_cp)
# # print(l3_cp.count(5))

# l3_cp.sort()
# # print(l3_cp)

# l3_cp.sort(reverse=True)
# # print(l3_cp)


# def sum_3(x,y,z):
#     return x+y+z

# print(sum_3(2,2,2))

# f = lambda x, y, z :  x + y + z
# print(f(2,2,2))

# test_array = [10, 11.5, 12, 13.5, 14,15]   

# print(test_array[2:3])

# a = [12,34,55]

# print(np.array(a))

# data = {'prodID': ['101', '102', '103', '104', '104'],

#             'prodname': ['X', 'Y', 'Z', 'X', 'W'],

#                 'profit': ['2738', '2727', '3497', '7347', '3743']}

# dataframe = pd.DataFrame(data)

# dataframe

# grouped_data = dataframe.groupby('prodID')

# print(grouped_data.max())

# demo_array = np.arange(10,17)

# demo_array [:]= 101

# print(demo_array)


# set1 = pd.Series(['A', 'B'])

# print(set1)
# df = pd.DataFrame(set1)
# print(df)
# new = ["P", "Q"]

# df['set2'] = new
# print(df)


squares = [x**2 for x in range(10)]
print(squares)

squares_str = [str(x) for x in squares]
print(squares_str)

squares_dt = [type(x) for x in squares_str]
print(squares_dt)
