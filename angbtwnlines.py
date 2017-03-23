# Given the x, y, and z location of a particle in three places, calculate the 
#   angle between the first two points and a detector in between the last two 
#   points and between the path of the outgoing particle(s) and the plane
#   then draw the path on a 3D plot

# DETECTOR SETUP
#    *             Incoming particle - Path vector denoted by I
#   -----------    Top GEM - Beam location in this plane denoted by T
#   -----------    Middle GEM - Beam location in this plane denoted by M
#   -----------    Cherenkov Detector - Beam location in this plane denoted by D
#   -----------    Bottom GEM - Beam location in this plane denoted by B
#            *     Outgoing Particle - Path vector denoted by O

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Set the information from GEMs
Tx = 1.0
Ty = 1.0
Mx = 2.0
My = 2.0
Bx = 6.0
By = 6.0

# Set the knowns
W1 = 5.0
W2 = 5.0
W3 = 2.5
Bz = 0.0 
Dz = Bz + W1
Mz = Bz + W1 + W2
Tz = Bz + W1 + W2 + W3

# Create Incoming Vector I
Ix = Mx - Tx
Iy = My - Ty
Iz = Mz - Tz

#Calculate angle between Incoming Vector and detector plane in degrees
I_Ang = -1.0 * np.degrees(np.arcsin( Iz / ( Ix**2 + Iy**2 + Iz**2 )**0.5 ))
print("Ray's incoming angle: ", I_Ang)

#Calculate Dx and Dy
slopex = (Mx - Tx) / (Mz - Tz)
Dx = Tx + slopex * (Dz - Mz)
slopey = (My - Ty) / (Mz - Ty)
Dy = My + slopey * (Dz - Mz)
print("The ray hits the detector at ({}, {}, {})".format(Dx, Dy, Dz))

#Create Outgoing Vector with Dx, Dy, and Dz
Ox = Bx - Dx
Oy = By - Dy
Oz = Bz - Dz

#Calculate angle between Outgoing Vector and detector plane in degrees
O_Ang = -1 * np.degrees(np.arcsin( Oz / ( Ox**2 + Oy**2 + Oz**2 )**0.5 ))
print("Ray's outgoing angle: ", O_Ang)

# Plot the points on a graph
fig = plt.figure()
ax = fig.gca(projection='3d')
xpoints = [Tx, Mx, Dx, Bx]
ypoints = [Ty, My, Dy, By]
zpoints = [Tz, Mz, Dz, Bz]
ax.plot(xpoints, ypoints, zpoints)
plt.show()
