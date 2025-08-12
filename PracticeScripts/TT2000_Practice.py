

# --- Description: Convert datetimes into TT2000 ---

# generate some datetimes
import datetime as dt
time1_dt = dt.datetime(2024,11,13,11,40,20, 500000)
time2_dt = dt.datetime(2015,8,25)

# Convert datetime into TT2000
import spaceToolsLib as stl
stl.setupPYCDF()
from spacepy import pycdf

time1_TT2000 = pycdf.lib.datetime_to_tt2000(time1_dt)
time2_TT2000 = pycdf.lib.datetime_to_tt2000(time2_dt)

print(time1_dt - time2_dt)
print(time1_TT2000 - time2_TT2000)


