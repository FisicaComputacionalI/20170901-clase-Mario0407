# lineplot.py
import numpy as np
import pylab as pl
# make an array of x values
x = [1,2,3,4,5]
# make an array of y values for each x value
y = [1,4,9,16,25]
# use pylab to plot x and y
pl.plot (x,y)
# show the plot on the screen
pl.savefig('templ.png')
