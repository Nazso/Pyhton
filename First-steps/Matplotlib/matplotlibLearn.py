"""
What is Matplotlib?
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C,
Objective-C and Javascript for Platform compatibility.
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

If we need to plot a line from (1, 3) to (8, 10),
we have to pass two arrays [1, 8] and [3, 10] to the plot function.

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

# xpoints = np.array([4, 8])
# ypoints = np.array([4, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

"""
Multiple Points
You can plot as many points as you like, just make sure you have the same number of points in both axis.

Example
Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
"""

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

"""
Default X-Points
If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc.,
depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

Example
Plotting without x-points:
"""

# xpoints = np.array([2, 4, 6, 8, 10, 12])
# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(xpoints, ypoints)
# plt.show()

print("------------------------Markers-------------------------")

"""
Markers
You can use the keyword argument marker to emphasize each point with a specified marker:

ExampleGet your own Python Server
Mark each point with a circle:
"""

# import matplotlib.pyplot as plt
# import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')
# plt.plot(ypoints, marker = '*')
# plt.plot(ypoints, marker = 's')
# plt.plot(ypoints, marker = '4')
# plt.plot(ypoints, marker = 'D')
# plt.show()

"""
Marker Reference
You can choose any of these markers:

Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
"""

print("----------------------fmt-----------------------")

"""
Format Strings fmt
You can also use the shortcut string notation parameter to specify the marker.

This parameter is also called fmt, and is written with this syntax:

marker|line|color
Example
Mark each point with a circle:
"""

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o:r')
# plt.plot(ypoints, 'D:g')
# plt.plot(ypoints, '*:b')
# plt.plot(ypoints, '*-.b')
# plt.show()

"""
The marker value can be anything from the Marker Reference above.

The line value can be one of the following:

Line Reference
Line Syntax	Description
'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
"""

# Note: If you leave out the line value in the fmt parameter, no line will be plotted.

"""
The short color value can be one of the following:

Color Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""

print("---------------------Marker size-------------------")

"""
Marker Size
You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

Example
Set the size of the markers to 20:
"""

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.plot(ypoints, marker = 'D', ms = 15)
# plt.plot(ypoints, marker = '*', ms = 30)
# plt.show()

print("--------------------marker color--------------------")

"""
Marker Color
You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:

Example
Set the EDGE color to red:
"""

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.plot(ypoints, marker = '*', ms = 20, mec = 'm')
# plt.show()

"""
You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:

Example
Set the FACE color to red:
"""

# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.plot(ypoints, marker = '*', ms = 20, mfc = 'm')
# plt.plot(ypoints, marker = '*', ms = 20, mec = 'g', mfc = 'm')
# plt.plot(ypoints, marker = '*', ms = 20, mec = 'y', mfc = 'm')
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#FF1111')
# plt.show()


print("--------------------linestyle--------------------")

# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

ypoints = np.array([3, 2, 5, 10])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()

"""
The line style can be written in a shorter syntax:

linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.
"""

# plt.plot(ypoints, ls = ':')
# plt.plot(ypoints, ls = '--')
# plt.show()

"""
Line Styles
You can choose any of these styles:

Style	            Or
'solid' (default)	'-'	
'dotted'	        ':'	
'dashed'	        '--'	
'dashdot'	        '-.'	
'None'	            '' or ' '
"""

"""
Line Color
You can use the keyword argument color or the shorter c to set the color of the line:

Example
Set the line color to red:
"""

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r')
# plt.plot(ypoints, c = '#4CAF50')
# plt.plot(ypoints, c = 'hotpink')
# plt.show()

"""
Line Width
You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is a floating number, in points:
"""

# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

"""
Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:

Example
Draw two lines by specifying a plt.plot() function for each line:
"""

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
