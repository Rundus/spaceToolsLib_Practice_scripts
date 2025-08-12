import matplotlib.pyplot as plt


xData = [3*(i+1) for i in range(5)]
yData = [9*(i+1) for i in range(5)]


# SIMPLE WAY - NON-OBJECT ORIENTED
# plt.scatter(xData, yData)
# plt.xlabel('x numbers')
# plt.ylabel('y numbers')
# plt.show()

# NOT SIMPLE WAY - OBJECT OREINTED
fig, ax = plt.subplots(nrows=2)
ax[0].plot(xData,yData)
ax[0].set_xlabel('x numbers')
ax[0].set_ylabel('y numbers')

ax[1].plot(xData,yData)
ax[1].set_xlabel('x numbers')
ax[1].set_ylabel('y numbers')
plt.show()