
# imports
from glob import glob
import io

import numpy as np

# get all the text files
path_to_folder = 'C:\Data\ACESII\L3\MPI\low'
text_file_paths = glob(path_to_folder+'\\*.txt*')

# print the file names
# for path in text_file_paths:
#     print(path)


# Load JUST ONE .txt file
file = text_file_paths[1] # note: index 1 is the data description
temp_data = []

with io.open(file, mode="r", encoding="utf-8") as f:

    next(f) # this skips the first line in the .txt file
    for line in f:
        temp_data.append([float(val) for val in line.split()])

    temp_data = np.array(temp_data).T

#     for line in f:
#         temp_arr_str = line.split()
#         temp_arr_float = [float(thing) for thing in temp_arr_str]
#         temp_data.append(temp_arr_float)
#
# data = np.array(temp_data)
# var1 = data[:, 0]
# print(var1)


