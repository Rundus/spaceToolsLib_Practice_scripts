

########################
# --- AND STATEMENTS ---
########################

# SYNTAX
# and

# y = 5
# x = 6
# z = 4
# if (y == x and y == z) and (x == y and x == z):
#     print('potato')
# else:
#     print(1)


########################
# --- NOT STATEMENTS ---
########################

# SYNTAX:
# not, !


# x, name = 5, "Connor"
# print(x,name)

# x = False
# if x is not True:
#     print('potato')

# y = [[1], [2], [3], [5, 6, 7]]
# if not [1] in y:
#     print('This is a happy potato')
# else:
#     print('This is a sad potato')

# z,k = 1,5
#
# if z == 1:
#     print('spud')
#     if k != 2 :
#         print('tuber')


##################################
# --- INEQUAILITIES STATEMENTS ---
##################################

# SYNTAX:
# <, >, <=, >=


# x, y = 4, 10
# if x >= 4 and y <= 9:
#     print('spud')

# COMPARING LISTS
# z, j = [5, 6], [5, 6]
# if z == j:
#     print('test')

#######################
# --- IN STATEMENTS ---
#######################

# SYNTAX:
# in

# a = [1,2,3,4,5]
# if 5 in a:
#     print('test')
# for thing in a:
#     print(thing)


# b = [[1,2,3],'Dog',(1,2,3),6, {'key1':[1,2,34],'key2':[1,2,3]}] # List containing: A list, string, integer, tuple, dictionary
# for thing in b:
#     print(thing)



#########################
# --- RANGE/ENUMERATE ---
#########################


# RANGE
# A = range(1, 6, 1)
# for thing in A:
#     print(thing)

# ENUMERATE
# B = [10,14,14,88,91]
#
# for idx, thing in enumerate(B):
#     print(thing)

# x,y = [1,2]
# print(x,y)

####################
# --- APPENDING  ---
####################
# a = [1,2,3]
# a.append([1,2,3])
# print(a)

# c = []
# for val in range(1000):
#     c.append(val)
# print(c)

####################################
# --- FOR LOOPS - SPECIAL SYNTAX ---
####################################

# L = [[1,2], [3,4], [5,6]]
# for subList in L:
#     x,y = subList

# for val in range(5):
#     print(val)



###########################
#### LIST COMPREHENSION ###
###########################
# a = []
# for val in range(5):
#     a.append(val)

a = [val/10 for val in [1,2,3,4,5]]
print(a)




