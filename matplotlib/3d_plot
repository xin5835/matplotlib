# 3d plot with matplotlib

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)

# height value
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')



ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')


ax.set_zlim(-2, 2)
 
plt.show()
