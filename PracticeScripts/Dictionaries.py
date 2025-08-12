# IMPORTS
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

# TOGGLES
wFile = 1
wKey = 5


# --- PROGRAM START ---

# get input Files
folderPath = r'C:\Users\cfelt\Desktop\sweptLP_calFiles_ACESII\*'
myFiles = glob(folderPath)

# Load in the data
df = pd.read_csv(myFiles[wFile])
dictKeys = df.keys()

# extract time data
timeData = df[dictKeys[0]]


# PLOT THE DATA
fig, ax = plt.subplots(nrows=len(dictKeys), ncols=1)
for i in range(len(dictKeys)):
    ax[i].plot(timeData, df[dictKeys[i]])
    ax[i].set_title(f'{dictKeys[i]} vs. {dictKeys[0]}')
    ax[i].set_xlabel(f'{dictKeys[0]}')
    ax[i].set_ylabel(f'{dictKeys[i]}')
plt.show()





