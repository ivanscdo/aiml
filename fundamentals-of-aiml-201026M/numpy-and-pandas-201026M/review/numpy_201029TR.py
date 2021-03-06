import numpy as np

### 00 NUMPY INTRO
vec = np.array([1,2,3])
# print('###vec:')
# print(vec)

mat = np.array([[0,1,2,3,4], [3,4,5,6,7], [6,7,8,9,10]])
# mat = np.array([[1,2,1],[4,5,9],[1,8,9]])

# print('###mat:')
# print(mat)

vec2 = np.arange(0,10)
# print('###vec2')
# print(vec2)

mat2 = np.array([np.arange(0,10),np.arange(0,10), np.arange(0,10)])
# print('###mat2')
# print(mat2)

vec3 = np.arange(0,10,2)
# print('###vec3')
# print(vec3)

vec4 = np.linspace(0,5,10)
# print('###vec4')
# print(vec4)
# print('###vec4.reshaped')
# print(vec4.reshape(5,2))

# print(mat)
# print(vec)
# prod = np.matmul(mat,vec)
# print(prod)

# print(np.linalg.solve(mat,prod))

index_vec = [0,1]
# print(vec[index_vec])

# print(mat[0][2])
# print(mat[0:2,1:3])

# vec[0:10] = 99
# print(vec)

# print(mat)
# mat[0:2,2:4] = 99
# print(mat)

# print(vec2)
vec2[3:6] = [1,2,3]
# print(vec2)

### 01 NUMPY ACCESSING ENTRIES
# rand_mat = np.random.rand(5,5)
# sub_mat = rand_mat[0:2, 0:3]
# print(rand_mat)
# print()
# print(sub_mat)
# sub_mat[:] = 99
# print()
# print()
# print(rand_mat)
# print()
# print(sub_mat)

mat3 = np.array([np.arange(0,10), np.arange(0,10), np.arange(0,10)])
# print(mat3)
# sub_mat3 = mat3[0:2,0:3]
# print()
# print(sub_mat3)
# sub_mat3[:] = 99
# print()
# print(mat3)
# print()
# print(sub_mat3)
# print()
sub_mat3_copy = mat3[0:2,0:3].copy()
sub_mat3_copy[:] = 99
# print(sub_mat3_copy)
# print()
# print(mat3)

### 02 SAVING LOADING NYMPY ARRAYS
rand_vec = np.random.randn(15)
print(rand_vec)
print(rand_vec>0)
print(rand_vec[rand_vec>0])

