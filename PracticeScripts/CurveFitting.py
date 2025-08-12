# --- Scipy Curve Fit Example ---

# --- Import some libraries ---
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# --- TOGGLES ---
PlotFakeData = True
# --- --- --- ---



# --- create some fake data ---
N = 25
xData = np.linspace(1, 100, N)
np.random.seed(105)
yData = np.array([val + 100*np.random.rand(1)*sum(np.random.rand(5)) for val in xData]).transpose()[0]


# --- Create Curve Fitting Function ---
def linearFunc(x, m, b):
    return m*x + b

# --- Use function with scipy.optimize.curve_fit to fit the data ---
params,cov = curve_fit(linearFunc,xData, yData)

# create the fitted data line
yData_fit = linearFunc(xData,*params)

# --- Plot the data and curve ---
if PlotFakeData:
    fig, ax = plt.subplots()
    ax.scatter(xData,yData, color='tab:blue')
    ax.plot(xData,yData_fit,color='red', label=f'm = {params[0]}\nb ={params[1]}')
    ax.legend()
    ax.set_xlim(0,200)
    ax.set_ylim(0, 200)
    plt.show()
