"""
What is Matplotlib?
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.
"""

import matplotlib

print(matplotlib.__version__)

print("---------------------------------Pyplot----------------------------------")

"""
Matplotlib Pyplot
Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

import matplotlib.pyplot as plt
Now the Pyplot package can be referred to as plt.

Example
Draw a line in a diagram from position (0,0) to position (6,250):
"""

import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 60])
# ypoints = np.array([0, 200])

# plt.plot(xpoints, ypoints)
# plt.show()

print("---------------------------------Plotting----------------------------------")

"""
Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
Example
Draw a line in a diagram from position (1, 3) to position (8, 10):
"""

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

"""
The x-axis is the horizontal axis.

The y-axis is the vertical axis.
"""

"""
Plotting Without Line
To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

Example
Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
"""

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
