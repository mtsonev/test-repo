# Given three points at three different heights, calculate the angle between the
#    lines drawn from the top point, to the middle, to the bottom
#    and then draw the lines

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Set the heights
z1 = 10
z2 = 6
z3 = 1

# Get X and Y coordinates
x1 = int(input("X coordinate of top point:"))
y1 = int(input("Y coordinate of top point:"))
x2 = int(input("X coordinate of middle point:"))
y2 = int(input("Y coordinate of middle point:"))
x3 = int(input("X coordinate of bottom point:"))
y3 = int(input("Y coordinate of bottom point:"))

# Get slopes of each line
m1 = (y1 - y2) / (x1 - x2)             #Line 1 connects points 1 and 2
m2 = (-1) * (y2 - y3) / (x2 - x3)      #Line 2 connects points 2 and 3

# Calculate angle between line and horizontal
ang1 = np.degrees(np.arctan(m1))
ang2 = np.degrees(np.arctan(m2))

# Calculate angle between the two lines
angtot = ang1 + ang2
print("Angle between lines is {0}".format(angtot))

# Plot the points on a graph
fig = plt.figure()
ax = fig.gca(projection='3d')
xpoints = [x1, x2, x3]
ypoints = [y1, y2, y3]
zpoints = [z1, z2, z3]
ax.plot(xpoints, ypoints, zpoints)
plt.show()
