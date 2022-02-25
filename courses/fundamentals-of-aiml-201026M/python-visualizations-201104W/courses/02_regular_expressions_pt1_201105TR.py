import re

# triple single quote allows you to enter newlines etc
text_to_search = '''
abcdefghijklmnpoqrstuvwxyz
ABCDEFGHIJKLMNPOQRSTUVWXYZ
1234567890
123abc

Hello HelloHello

MetaCharacters (Need to be escaped):
.^ $ * + ?  ( ) [ ] / | ( )

utexas.edu

321-555-4321
321.555.1234

daniel-mitchell@utexas.edu

Mr. Johnson
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# r - raw string
# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)

# for mat in matches:
#     print(mat)

# . - special character in regex
# pattern = re.compile(r'\.')
# matches = pattern.finditer(text_to_search)
# count = 0
# for mat in matches:
#     count += 1
#     print(mat)
#     print(count)

# d - digit 0-9
# pattern = re.compile(r'\d')
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)

# D - NOT a digit 0-9
# pattern = re.compile(r'\D')
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)


# pattern = re.compile(r'\w')
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)

# pattern = re.compile(r'\d\w') # will not return 12 23; can't return overlapping characters
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)

# pattern = re.compile(r'\d\s') # any digit followed by a space
# matches = pattern.finditer(text_to_search)
# for mat in matches:
    # print(mat)

# \b - word boundary, 
# pattern = re.compile(r'\bHello\b')
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)


# pattern = re.compile(r'\BHello\b')
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)


# pattern = re.compile(r'\b\d')
# matches = pattern.finditer(text_to_search)
# for mat in matches:
#     print(mat)

pattern = re.compile(r'^\s')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)