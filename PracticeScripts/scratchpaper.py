
import spaceToolsLib as stl
import matplotlib.pyplot as plt

file = 'C:\Data\ACESII\L2\low\ACESII_36364_l2_langmuir.cdf'

data_dict = stl.loadDictFromFile(file)




plt.plot(data_dict['fixed_Epoch'][0], data_dict['fixed_current'][0])
plt.yscale('log')
plt.show()