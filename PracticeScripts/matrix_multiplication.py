import numpy as np

# --- 3x3 times 3x1 matrix multiply ---
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([1,2,3])
#
# print(np.matmul(a,b))


# --- rotation matrix: rotate (1,1,0) vector to align with the y-axis ---
# a = np.array([1,1,0])
# angle = -1*np.radians(45) # in deg
# Rz = np.array([
#     [np.cos(angle), -1*np.sin(angle), 0],
#     [np.sin(angle),    np.cos(angle), 0],
#     [0 ,                          0 , 1]
# ])
# print(np.matmul(Rz,a))

# --- get the magnitude of a vector ---
# print(np.linalg.norm(a))

# --- Go learn this function ---
# scipy.Cubicspline

#--- How to find a specific INDEX in an array ---
a = np.array([9,5,11,41])

print(np.abs(a - 41).argmin())

