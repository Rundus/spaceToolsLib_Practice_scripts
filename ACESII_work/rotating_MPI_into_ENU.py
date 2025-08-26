

# NOTES:

# -- GENERAL GOAL --
# [1] Get the MPI into the rocket coordinates
# [2] Apply the rkt DCM matrix to get MPI into ENU coordinates

# Example on how to perform [1] above
# (1) Pick MPI3
# (2) Define a MPI velocity vector: vec = [Vx, Vy, 0]
# (3) Perform 3D rotation matrices to get MPI3 coordinates aligned with Rocket Coordinates:
# (3a) First rotate MPI3 coordinates by 90deg about z-axis
# (3b) rotate again by -90deg about x-axis
# (4) Done with step [1], repeat for ALL MPIs
# (5) Store the MPI#_Vx, MPI#_Vy, MPI#_Vz and Epoch for all 4 MPIs into one datafile

# [2] Apply the DCM matrix to each MPI coordinate set to get MPI in ENU coordinates

# Things you'll need: Search numpy arrays for closest values e.g. Epoch of Attitude data and DCM matrix elements.

# A note on what the DCM is:
# The Discrete Cosine Matrix (DCM) is a 3x3 matrix which "un-despins" or despins the payload
# from a spinning frame into a static frame, such as ECEF or ENU. The DCM we have despins the rocket
# coordinates from Payload Coordinates into ENU coordnates.