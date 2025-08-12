
# imports
import spaceToolsLib as stl
from copy import deepcopy
import numpy as np

# [1] defining data_dict_output format

example_attrs = {'LABLAXIS': None,
                 'DEPEND_0': None,
                 'UNITS': None}

data_dict_output = {
    'arissa': [[], {}],
    'khan': [[], {}]
}

# [2] fill in the attributes of your data_dict_output
data_dict_output['arissa'][1] = deepcopy(example_attrs)
data_dict_output['khan'][1] = deepcopy(example_attrs)

# actually update your attributes
data_dict_output['arissa'][1]['UNITS'] = 'm'
data_dict_output['arissa'][1]['LABLAXIS'] = 'Human?'

data_dict_output['khan'][1]['UNITS'] = 'feet'
data_dict_output['khan'][1]['DEPEND_0'] = 'arissa'

# fill in some test data
data_dict_output['arissa'][0] = np.array([0, 1, 2, 3, 4]) #data MUST be numpy arrays when outputting a .cdf
data_dict_output['khan'][0] = np.array([33, 36, 39, 42, 45]) #data MUST be numpy arrays when outputting a .cdf


# [3] actually outputting the data
file_out_path = r'C:\Users\cfelt\OneDrive - University of Iowa\test.cdf'
stl.outputCDFdata(outputPath=file_out_path, data_dict=data_dict_output)