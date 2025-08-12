# todo list
# [1] how to use spacetoolslib to load .cdf files
# [2] how to read .txt files of the MPI data
# [3]

# imports
import spaceToolsLib as stl

# path to any particular .cdf file
path = 'C:\Data\ACESII\L2\high\ACESII_36359_l2_eepaa_fullCal.cdf'

# use spacetoolslib to load a python dictionary of all the data
data_dict = stl.loadDictFromFile(path)


# --- STRUCTURE OF THE DATA DICTIONARIES ---

# --- General Python dictionary format---
# dict = {
#   'key1': thing1,
#   'key2': thing2,
#    ... etc
# }

# --- SpaceToolsLib dictionary format ---
# data_dict = {
#   'key1': [data1, {attributes dictionary 1}],
#   'key2': [data2, {attributes dictionary 2}],
#    ... etc
# }

# [1] show all the keys of a python dictionary
key_names = data_dict.keys()
# print(key_names)

# [2] get a particular dataset
data1 = data_dict['Differential_Number_Flux'][0]
# print(data1)

# [3] Get the attributes of a particular dataset
attrs1 = data_dict['Differential_Number_Flux'][1]
# print(attrs1)


# [4] USE THE DEEPCOPY FUNCTION!!!!
from copy import deepcopy
# a = [1,2,3]
# print('a',a)
# b = a[1:3]
# print('b',b)
# a[1]=0
# print('b',b)

# Make two variables which are totally independent from one another
var1 = deepcopy(data_dict['Differential_Number_Flux'][0])
var2 = 5*deepcopy(var1)
print(var1[0][0][0])
print(var2[0][0][0])


