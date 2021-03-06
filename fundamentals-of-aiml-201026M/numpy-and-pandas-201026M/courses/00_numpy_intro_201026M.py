import numpy as np

### ADVANCED MATHEMATICS (MORE THAN ADDING, MULTIPLICATION, ETC)
# print(np.cos(np.pi))
# print(np.sqrt(1.21))
# print(np.log(np.exp(5.2)))


### CREATE ARRAY AND 2D ARRAY
vec = np.array([1,2,3])
# print(vec)
mat = np.array([[1,2,1],[4,5,9],[1,8,9]])
# print('')
# print(mat)
# print('')
# print(mat.T) # transpose matrix, i.e. switch rows & columns


### CREATE ARRAY WITH RANGE
vec2 = np.arange(0,15) # numpy array range
# print(vec2)
# print('')
vec3 = np.arange(3,21,6) # 3 - starting num, inclusive; 21 - ending num, exclusive; 6 - step size
# print(vec3)


### LINEAR SPACE AND RESHAPING
vec4 = np.linspace(0,5,10) # linear space; inclusive starting, inclusive ending, num of items (required)
# print(vec4)
# print('')
# print(vec4.reshape(5,2)) #transforms into matrix, 5 rows, 2 columns
vec4_reshaped = vec4.reshape(5,2) # .reshape is func, does not transform, would need to store output into var
# print(vec4_reshaped)
# print(vec4)


### CREATE ARRAY WITH ALL ZEROS, ONES, OR IDENTITY MATRIX
mat2 = np.zeros([5,3])
# print(mat2)
mat3 = np.ones((3,5))
# print('')
# print(mat3)
mat4 = np.eye(5) # identity matrix, all zeros, except for ones on main diagonal
# print('')
# print(mat4)


### OPERATIONS ON ARRAYS
vec5 = np.arange(1,6)
vec6 = np.arange(3,8)
# print(vec5)
# print(vec6)
# print(vec5+vec6) # first entry of vec5 + first entry of vec6, etc
# print(vec5*vec6)
# print(1/vec5) # 1 divided by each entry
# print(np.sqrt(vec6))


### MATRIX MULTIPLICATION FUNC
print(mat)
print('')
print(vec)
print()
product = np.matmul(mat,vec) # matrix multiplication
print(product)


### LINEAR ALGEBRA FUNC
print(np.linalg.solve(mat,product))
# print('')
# print(np.linalg.inv(mat))


### UNIQUE FUNC ON ARRAYS
# vec7 = np.array(['blue', 'red', 'orange', 'purple', 'purple', 'orange', 'Red', 6])
# print(vec7)
# print(np.unique(vec7))


### RANDOM.RAND FUNC
# rand_mat = np.random.rand(5,5) # uniform random variable; 5 rows, 5 columns
# print(rand_mat)
# rand_mat2 = np.random.randn(10,5) # standard normal random variable
# print('')
# print(rand_mat2)

### MIX MAX MEAN FUNC
# print(np.mean(rand_mat))
# print(np.std(rand_mat2))

# print(np.min(rand_mat))
# print(np.max(rand_mat2))
