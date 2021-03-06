import numpy as np

# l1 = [1,2,3,4]
# nd1 = np.array(l1)
# print(nd1)

# l2 = [5,6,7,8]
# nd2 = np.array([l1,l2])
# print(nd2)

# print(nd2.shape)
# print(nd2.size)
# print(nd2.dtype)

# id_mat = np.identity(3)
# print(id_mat)

mat00 = np.array([[9,8,7],[6,5,4],[3,2,1]])
# print(mat00)
mat01 = mat00.T
# print(mat01)
# print(mat00 + 1)

nd6 = np.array([[ 1, 4, 9, 121, 144, 169],[ 16, 25, 36, 196, 225, 256,],[ 49, 64, 81, 289, 324, 361]])
nd7 = np.matrix([[ 1, 4, 9, 121, 144, 169],[ 16, 25, 36, 196, 225, 256,],[ 49, 64, 81, 289, 324, 361]])

# print(nd6)

# print(type(nd6))
# print(type(nd7))
# print(nd6.mean())
# for num in nd6:
#     print(num.mean())




# print(np.dot(mat00,nd6))

x = np.arange(20)
print(x)
print(x[0:5])

print(x[::2])

print(x[::-1])