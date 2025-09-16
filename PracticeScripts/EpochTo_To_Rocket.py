# Example: Spacetoolslib function: EpochTo_T0_Rocket

import datetime as dt
import spaceToolsLib as stl

epoch = [dt.datetime(2022,11,20,17,20,0),
     dt.datetime(2022,11,20,17,20,1),
     dt.datetime(2022,11,20,17,20,2),
     dt.datetime(2022,11,20,17,20,3),
     dt.datetime(2022,11,20,17,20,4),
     dt.datetime(2022,11,20,17,20,5)]

T0 = dt.datetime(2022,11,20,17,19,0)

print(stl.EpochTo_T0_Rocket(InputEpoch=epoch,
                            T0=T0))



path_to_attitude = 'rrr'
path_to_MPI = 'rrrr'

data_dict_attitude
