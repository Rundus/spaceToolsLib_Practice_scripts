# imports
import spaceToolsLib as stl
from glob import glob
import matplotlib.pyplot as plt


# SpaceToolsLib has physics-related variables
# print(stl.Re) # Radius of the Earth (In kilometers)

# How to Open CDF files
folderNames = ['Current', 'Density']
folderPath = r"C:\Users\cfelt\Desktop\ACESII_Langmuir"
wVar = 1 # which physical variable
wFile = 1 # which file inside the variable folder


# Open the CDF file using spaceToolsLib "inputcdf
filePath = glob(folderPath + rf'\{folderNames[wVar]}\*') # returns a list of strings containing the absolute paths of the files
myDataFile = filePath[wFile] # select the specific file I want

data_dict = stl.loadDictFromFile(inputFilePath=myDataFile) # use spaceToolsLib to read a CDF file and output a "data dictionary"


# --- NOTE on data_dict ---
# Desciption: The stl.loadDictfromFile command outputs a python dictonary with the following format:
# data_dict = {
#               'key1':[DATA1, {DATA1 attributes dictionary}],
#               'key2':[DATA2, {DATA2 attributes dictionary}],
#               etc...
#               }

# key1 - the name of the first key/variable in the data_dict dictionary
# DATA1 - The actual dataset
# DATA1 attributes dictionary - python dictionary of attributes associated with DATA 1.
# --- --- --- --- --- ---


# EXAMPLE USAGE 1: Print all the keys in the data dictionary
# for key in data_dict.keys():
#     print(key)

# EXAMPLE USAGE 2: Access plasma density, epoch and plot it vs. time
# density = data_dict['ni'][0]
# epoch = data_dict['Epoch'][0]
#
# fig, ax = plt.subplots()
# ax.plot(epoch, density)
# plt.show()


# EXAMPLE USAGE 3: Write out your own datafile
# outputDataPath = r'C:\Users\cfelt\Desktop\ACESII_Langmuir\testFile.cdf'
# fakeData1 = [1, 2, 3]
# fakeData2 = [4, 5, 6]
# outputData = {'key1': [fakeData1, {'LABLNAM':'ArissaVar'}],
#               'key2':[fakeData2, {}]
#               }
# stl.outputCDFdata(outputPath=outputDataPath, data_dict=outputData)
