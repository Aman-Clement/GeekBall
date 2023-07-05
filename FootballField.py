# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:09:32 2023

@author: amanc
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

# Create figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# outer rectangle and center line
plt.plot([0, 0], [0, 90], color="green")
plt.plot([0, 130], [90, 90], color="green")
plt.plot([130, 130], [90, 0], color="green")
plt.plot([130, 0], [0, 0], color="green")
plt.plot([65, 65], [0, 90], color="green")

# centre circle and spot
centreCircle = plt.Circle((65, 45), 9.15, color="red", fill=False)
centreSpot = plt.Circle((65, 45), 0.8, color="blue")

ax.add_patch(centreCircle)
ax.add_patch(centreSpot)

# left penalty area
plt.plot([16.5, 16.5], [65, 25], color="green")
plt.plot([0, 16.5], [25, 25], color="green")
plt.plot([0, 16.5], [65, 65], color="green")

# right penalty area
plt.plot([113.5, 113.5], [65, 25], color="green")
plt.plot([130, 113.5], [25, 25], color="green")
plt.plot([130, 113.5], [65, 65], color="green")

# D arcs
rightArc = Arc((119, 45), height=18.3, width=18.3,
               angle=0, theta1=130, theta2=230)
ax.add_patch(rightArc)
leftArc = Arc((11, 45), height=18.3, width=18.3,
              angle=0, theta1=310, theta2=50)
ax.add_patch(leftArc)

# 6 yard box
plt.plot([130, 124.5], [54, 54], color="green")
plt.plot([124.5, 124.5], [54, 36], color="green")
plt.plot([124.5, 130], [36, 36], color="green")

plt.plot([0, 5.5], [54, 54], color="black")
plt.plot([5.5, 5.5], [54, 36], color="black")
plt.plot([5.5, 0.5], [36, 36], color="black")

# penalty spot
leftPenSpot = plt.Circle((11, 45), 0.8, color="black")
rightPenSpot = plt.Circle((119, 45), 0.8, color="black")
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)


plt.show()
