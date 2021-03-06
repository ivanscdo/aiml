import numpy as np

### BOOLEANS AS INDEX TO ACCESS ARRAY
# rand_vec = np.random.randn(15)
# print(rand_vec)
# print(rand_vec>0) # returns boolean if index is greater than 0
# print(rand_vec[rand_vec>0]) # prints the value at the index where greater than 0, i.e. true

### PERS EXAMPLE OF ABOVE
# ex_vec = np.array([0,1,2,3])
# ex_bool = np.array([True, True, False, False])
# print(ex_vec[ex_bool])

### BOOLEANS IN MATRICES
rand_mat2 = np.random.randn(10,5)
# print(rand_mat2)
# print(rand_mat2[rand_mat2>0]) # converts booleans in matrix to array

### MODIFY ALL VALUES OF ARRAY
# print(rand_vec)
# print()
# rand_vec[rand_vec>0.5] = -5 # modify all values that are greater than 0.5 to -5
# print(rand_vec)

### SAVING NUMPY ARRAY
# np.save('saved_file_name', rand_mat2) # only stores single array, does not work with multiple
# np.savez('zipped_file_name', rand_vec=rand_vec, rand_mat2=rand_mat2) # saves several arrays; z - zipp; <saved_array_in_zip> = <array_to_be_saved>

### LOADING SAVED FILE
loaded_vec = np.load('saved_file_name.npy')
loaded_zip = np.load('zipped_file_name.npz')

# print(loaded_vec)
# print()
# print(loaded_zip)

### NEED TO LOAD NPZ WITH NAME OF ARRAYS
# print(loaded_zip['rand_vec'])
# print()
# print(loaded_zip['rand_mat2'])
# new_array = loaded_zip['rand_vec']
# print(new_array)


### SAVE FILES INTO TEXT FILE
np.savetxt('text_file_name.txt', rand_mat2,delimiter=',') # can only store one array in text file
rand_mat2_txt = np.loadtxt('text_file_name.txt', delimiter=',')
print(rand_mat2)
print()
print(rand_mat2_txt)

