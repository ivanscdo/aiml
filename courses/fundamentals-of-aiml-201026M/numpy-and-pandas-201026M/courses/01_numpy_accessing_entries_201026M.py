import numpy as np

### CREATE ARRAY, ACCESS ARRAY
rand_vec = np.random.randn(19)
# print(rand_vec)
# print(rand_vec[6])
# print(rand_vec[4:9]) # inclusive:exclusive


### PASS ARRAY AS INDEX TO ACCESS ARRAY
# print(np.arange(0,15,3))
# print(rand_vec[np.arange(0,15,3)])


### PERS EX OF ABOVE
# ex_arr = np.array([0,1,2,3,4,5,6])
# ex_index = np.array([2,4,6])
# print(ex_arr[ex_index])


### ACCESSING MATRICES
rand_mat = np.random.rand(5,5)
print('rand_mat:')
print(rand_mat)
# print(rand_mat[1][2]) # row 2, column 3; 0-based index like arrays
# print(rand_mat[1,2]) # same as above
# print(rand_mat[0:2,1:3]) # first value inclusive, second exclusive; row 0-1, column 1-2


### ASSIGN ARRAY
# print(rand_vec)
# rand_vec[3:5] = 4 # assign index 3 thru 4 to 0
# print('post 4:')
# print(rand_vec)
# rand_vec[3:5] = [1,2]
# print('post [1,2]:')
# print(rand_vec)


### ASSIGN MATRIX
# print(rand_mat)
# rand_mat[1:3,3:5] = 0 # assign row 1 thru 2 & column 3 thru 4 to 0
# print('')
# print(rand_mat)


### VEC=ARRAY, MATRIX=2D ARRAY
# ex_vec = np.random.rand(5)
# ex_mat = np.random.rand(5,5)
# print(ex_vec)
# print(ex_mat)


### SUB MATRIX, EDIT SUB & ORIGINAL
sub_mat = rand_mat[0:2,0:3]
print('sub_mat:')
print(sub_mat)
# sub_mat[:] = 3 # re-assigns all values to 3
# print('sub_mat all 3:')
# print(sub_mat)
# print('rand_mat:')
# print(rand_mat) # modifying sub matrix, also modifies original matrix. will need to copy w/ .copy()


### COPY MATRIX, EDIT COPY W/O EDITING ORIGINAL
sub_mat2 = rand_mat[0:2,0:3].copy()
sub_mat2[:] = 99
print('sub_mat2: ')
print(sub_mat2)
print('rand_mat:')
print(rand_mat)


