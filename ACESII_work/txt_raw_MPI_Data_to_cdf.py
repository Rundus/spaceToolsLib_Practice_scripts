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
import time
import datetime as dt
from copy import deepcopy


# Time your code
start_time = time.time()



### MAIN FUNCTION ###
def txt_raw_MPI_Data_to_cdf():

    # Load in the .txt files
    stl.prgMsg('Loading the data')
    path_to_data = 'C:\Data\ACESII\L3\MPI\low\\'
    data_file_names = glob(path_to_data + '*MPI*' +'*.txt')

    # prepare the output
    data_dict_output = {}

    # strip the data out of each file and append it to the data_dict_output
    for txtfile in data_file_names:
        temp_data = [] # put this initialization in the loop so we have a "fresh list" each iteration

        with io.open(txtfile, mode="r", encoding="utf-8") as f:
            next(f)  # this skips the first line in the .txt file
            for line in f:
                temp_data.append([float(val) for val in line.split()])

            temp_data = np.array(temp_data,dtype='float64').T


        # Correct T0 point of Epoch in temp_data
        T0 = dt.datetime(1900, 1, 1) # Jan 1st, 1900
        Epoch = np.array([T0 + dt.timedelta(seconds=tme) for tme in temp_data[0]])

        # APPEND file data into data_dict_output
        if 'MPI1' in txtfile:
            counter = 1
        elif 'MPI2' in txtfile:
            counter = 2
        elif 'MPI3' in txtfile:
            counter = 3
        elif 'MPI4' in txtfile:
            counter = 4

        data_dict_output = {**data_dict_output,
                            **{f'Epoch_MPI{counter}':[np.array(Epoch), {'LABLAXIS':'Epoch','UNITS':None,'DEPEND_0':f'Epoch_MPI{counter}'}],
                               f'Vx_rkt_MPI{counter}':[np.array(temp_data[1]), {'LABLAXIS':'Vx in rocket frame','UNITS':'m/s','DEPEND_0':f'Epoch_MPI{counter}'}],
                               f'Vy_rkt_MPI{counter}':[np.array(temp_data[2]), {'LABLAXIS':'Vy in rocket frame','UNITS':'m/s','DEPEND_0':f'Epoch_MPI{counter}'}]}
                            }
    stl.Done(start_time)


    # write out the data
    stl.prgMsg('Writing out the data')
    outputPath = 'C:\Data\ACESII\L3\MPI\low\\'
    file_out_name = 'ACESII_36364_l3_MPI.cdf'
    stl.outputCDFdata(outputPath=outputPath+file_out_name, data_dict=data_dict_output)
    stl.Done(start_time)


### EXECUTE ###
txt_raw_MPI_Data_to_cdf()