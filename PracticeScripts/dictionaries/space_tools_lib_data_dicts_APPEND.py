
import numpy as np

data_dict_output = {} # initialize the data dictionary
print(data_dict_output)

# APPEND some data to the data_dict_output dictionary
data_dict_output = {**data_dict_output,
                    **{
                        'key1':[np.array([1,2,3]),{}],
                        'key2':[np.array([1,2,3]),{}]
                        # etc
                       }
                    }
print(data_dict_output)


