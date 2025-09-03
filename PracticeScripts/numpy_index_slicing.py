

import numpy as np

a = np.array([3*i for i in range(1,5+1)])
print('Original Array',a)

print("first three values", a[0:3])

# everything above 9
print("everything above 9", a[3:])


# everything!
print("everything! ", a[0:])

# everything!
print("everything! (again) ", a[:])