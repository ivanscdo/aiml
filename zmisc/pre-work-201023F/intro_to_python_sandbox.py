### indexed data structure, mutable
# list = ['red', 'wine', 'success']
# print(type(list)) #<type 'list'>


# rws = 'red wine, success!'
# outer_list = [list, rws]
# print(outer_list[0][1])

# for i in outer_list:
#     for j in i:
#         print(j)



# outer_list_copy = outer_list.copy
# outer_list_copy[1] = list
# print(outer_list_copy)

### indexed data structure, immutable
# tuple = ('red', 'wine', 'success')
# tuple[3] = 'white'
# print(tuple)


### unindexed data structure, mutable, can only have unique values
# set = {'red', 'wine', 'success'}
# set.add('rws')
# set.add('red')
# print(set)

# set_too = {'red', 'wine', 'success', 'white'}
# isDisjointed = str(set.isdisjoint(set_too))
# difference = str(set.difference(set_too))

# print('isDisjointed: ' + isDisjointed)
# print(set_too.difference(set))

# set02 = {'rws', 'red'}

# print(set.isdisjoint(set02))

# set03 = set.intersection(set02)

# print(set03)



# dict = {
#     'red': 'devil',
#     'wine': 'wino',
#     'success': 'work'
# }

# print(dict)

# dict['red'] = 'wine'

# print(dict)



# for_loop_list = ['red', 'wine', 'success']
# for element in for_loop_list:
#     print(element)
# print(for_loop_list)



# print(range(6))
# print(range(4,10,))
# print(range(4,10,2))
# print(range(4,10,3))

# for num in range(6):
#     print(num)

# for num in range(4,10):
#     print(num)



# i = 6
# while i < 10:
#     print(i)
#     i+=1



# rws = 'red wine, success!'
# rws = 'rws'
# rws = 0

# if rws == 'red wine, success!':
#     print('if')
# elif rws == 'rws':
#     print('elif')
# else:
#     print('else')

# def x2p7(x):
#     squ = x ** 2
#     squ_plus7 = squ + 7
#     return squ_plus7

# ans = x2p7(3)
# print(ans)

# def func(x,y):
#     lenx = len(x)
#     leny = len(y)
#     z = [0]*(lenx*leny)
#     counter = 0
#     for i in x:
#         for j in y:
#             z[counter] = i*j
#             counter = counter+1
#     return z
# x = [1, 3, 5]
# y = [2, 4, 6]
# output = func(x,y)
# print(output)

# x2p7v2 = lambda x: x**2+7

# print(x2p7v2(2)) 

# lamba_func = lambda x,y,z: (x*x+y)/z

# print(lamba_func(2,6,2))

# class My_class:
#     def init(self, var2):
#         self.first_var = 2
#         self.second_var = var2
#     def multiply_vars(self):
#         return self.first_var * self.second_var

# class_ex = My_class()
# class_ex.init(2)
# print(class_ex.first_var)
# print(class_ex.second_var)
# print(class_ex.multiply_vars())


# class_ex.third_var = 4
# print(class_ex.third_var)


# class Pet:
#     def __init__(self, animal_type, name, age, weight_lbs, color):
#         self.animal_type = animal_type
#         self.name = name
#         self.age = age
#         self.weight_lbs = weight_lbs
#         self.color = color
#         self.weight_kg = self.calc_weight_in_kg()
    
#     def calc_weight_in_kg(self):
#         return 0.453592 * self.weight_lbs

#     def describe_pet(self):
#         print('This pet is a ', self.color, self.animal_type)

# pen = Pet('dog', 'Penny', '8 yrs', 50, 'white & brown')
# pen.describe_pet()


# import os

# print(os.name)
# print(os.getcwd())
# print(os.listdir('.'))
# os.mkdir(<path_to_dir>)
# os.rename(<path_to_old_dir>, <path_to_new_dir>)

# file.open(<path_to_file>, <r_or_w>)
# file.write(<string_to_write>)
# file.close()

# d = {'Name':'John Wick','Age':47,'Address':'NY'}  
# # d = {}  
# print(d)

# dd = d.fromkeys(list('ABCD')) 
# # print(list('ABCD'))
# # print(dd)

# print(d['Name'])

a = input()
