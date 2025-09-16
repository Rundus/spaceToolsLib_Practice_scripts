# --- MPI_instrFrm_to_rktFrm.py ---
# Description: take the MPI data in instrument frame and
# convert rotate it to rocket frame


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
def MPI_instrFrm_to_rktFrm():

    # Load in the .cdf files
    stl.prgMsg('Loading the data')
    path_to_data = 'C:\Data\ACESII\L1\low\MPI\\'
    file_name = glob(path_to_data + "*.cdf*")[0]
    data_dict = stl.loadDictFromFile(file_name)
    stl.Done(start_time)


    # prepare the output
    data_dict_output = {
        'Epoch_MPI1': deepcopy(data_dict['Epoch_MPI1']),
        'Epoch_MPI2': deepcopy(data_dict['Epoch_MPI2']),
        'Epoch_MPI3': deepcopy(data_dict['Epoch_MPI3']),
        'Epoch_MPI4': deepcopy(data_dict['Epoch_MPI4']),
    }


    stl.prgMsg('Rotating MPI Data')
    for idx in range(4):

        Vx = data_dict[f'Vx_rkt_MPI{idx+1}'][0]
        Vy = data_dict[f'Vy_rkt_MPI{idx + 1}'][0]
        Vz = np.zeros(shape=len(Vx))
        vec_instr = np.array([Vx,Vy,Vz]).T

        if idx == 0: # MPI1
            R1 = stl.Rx(90)
            R2 = stl.Ry(90)
            vec_rkt = np.array([R2 @ (R1 @ v) for v in vec_instr])

        elif idx == 1: # MPI2
            R1 = stl.Rz(90)
            vec_rkt = np.array([R1 @ v for v in vec_instr])

        elif idx == 2:  # MPI3
            R1 = stl.Ry(-90)
            R2 = stl.Rz(90)
            vec_rkt = np.array([R2 @ (R1 @ v) for v in vec_instr])

        elif idx == 3:  # MPI4
            R1 = stl.Ry(180)
            R2 = stl.Rz(90)
            vec_rkt = np.array([R2 @ (R1 @ v) for v in vec_instr])

        # store the data
        data_dict_output = {**data_dict_output,
                            **{
                                f'Vx_rkt_MPI{idx + 1}': [vec_rkt[:, 0], {'DEPEND_0':f'Epoch_MPI{idx+1}','LABLAXIS':f'Vx_rkt_MPI{idx + 1}'}],
                                f'Vy_rkt_MPI{idx + 1}': [vec_rkt[:, 1], {'DEPEND_0':f'Epoch_MPI{idx+1}','LABLAXIS':f'Vy_rkt_MPI{idx + 1}'}],
                                f'Vz_rkt_MPI{idx + 1}': [vec_rkt[:, 2], {'DEPEND_0':f'Epoch_MPI{idx+1}','LABLAXIS':f'Vz_rkt_MPI{idx + 1}'}],
                            }
                            }

    stl.Done(start_time)


    # write out the data
    stl.prgMsg('Writing out the data')
    outputPath = 'C:\Data\ACESII\L1\low\\'
    file_out_name = 'ACESII_36364_l1_MPI_rktFrm.cdf'
    stl.outputCDFdata(outputPath=outputPath+file_out_name, data_dict=data_dict_output)
    stl.Done(start_time)


### EXECUTE ###
MPI_instrFrm_to_rktFrm()