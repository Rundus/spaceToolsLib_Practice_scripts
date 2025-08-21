# --- txt_raw_MPI_Data_to_cdf.py ---
# Description: takes the ACSE-II raw MPI data in .txt files
# and converts them to .cdf using spacetoolslib library.


# --- --- --- ---
# --- IMPORTS ---
# --- --- --- ---
import spaceToolsLib as stl
from copy import copy
from glob import glob
import numpy as np
import io



### MAIN FUNCTION ###
def txt_raw_MPI_Data_to_cdf():

    # Load in the .txt files
    path_to_data = 'C:\Data\ACESII\L3\MPI\low\\'
    data_file_names = glob(path_to_data + '*MPI*')

    # prepare the output
    data_dict_output = {}

    # strip the data out of each file and append it to the data_dict_output
    for txtfile in data_file_names:
        temp_data = [] # put this initialization in the loop so we have a "fresh list" each iteration

        with io.open(txtfile, mode="r", encoding="utf-8") as f:
            next(f)  # this skips the first line in the .txt file
            for line in f:
                temp_data.append([float(val) for val in line.split()])

            temp_data = np.array(temp_data).T

        # APPEND file data into data_dict_output
        data_dict_output = {**data_dict_output,
                            **{'Epoch':[np.array(temp_data[0]), {'LABLAXIS':'Epoch','UNITS':None,'DEPEND_0':'Epoch'}],
                               'Vx_rkt':[np.array(temp_data[1]), {'LABLAXIS':'Vx in rocket frame','UNITS':'m/s','DEPEND_0':'Epoch'}],
                               'Vy_rkt':[np.array(temp_data[2]), {'LABLAXIS':'Vy in rocket frame','UNITS':'m/s','DEPEND_0':'Epoch'}]}
                            }

    # organize the data_dict_output

    # write out the data


### EXECUTE ###
txt_raw_MPI_Data_to_cdf()