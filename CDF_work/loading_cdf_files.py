# [1] how to use spacetoolslib to load .cdf files
# [2] how to read .txt files of the MPI data
# [3]

# imports
import spaceToolsLib as stl

path = 'C:\Data\ACESII\L2\high\ACESII_36359_l2_eepaa_fullCal.cdf'

data_dict = stl.loadDictFromFile(path)