''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''


import numpy as np
import time
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
from bokeh.charts import Scatter
import bokeh.palettes


# Set up data
counter = 1

N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))





def update_func():
    #global counter
    #counter = counter + 1
    update_func.counter +=1
    if True:
        
        x = np.linspace(0, 4*np.pi, N)
        y = np.sin(x + update_func.counter/10)
    else:
        x = np.linspace(0, 4*np.pi, N)
        y = 0*np.sin(x + counter)
    source.data = dict(x=x, y=y)
update_func.counter = 0


# Set up plot
plot = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])
plot2 = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0,100], y_range=[0, 100])
laser = np.loadtxt("C:\\Users\\Oleksiy\\Desktop\\Code\\PyExamples\\laserspot.txt")
plot2.image(image=[laser],x=[0],y=[0],dw=[100],dh=[100],palette=bokeh.palettes.viridis(256))


plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
#plot.line(x, y, line_width=3, line_alpha=0.6)


curdoc().add_root(row(plot,plot2, width=800))
curdoc().add_periodic_callback(update_func,1000)
curdoc().title = "Sliders"