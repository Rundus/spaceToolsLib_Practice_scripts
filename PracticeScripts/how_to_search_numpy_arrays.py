import numpy as np


a = np.array([3,6,9,12,15])
search_item = 9

print(np.abs(a - search_item).argmin())

# This works on datetimes too!
