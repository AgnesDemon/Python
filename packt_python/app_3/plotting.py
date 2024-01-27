#This should access the data from the webcam and create a bar graph with that data that shows when motion is detected
#from controlling_the_webcam_and_detecting_objects import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import pandas

df = pandas.read_csv("Times.csv")
#print(df)
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(width=500, height=100, x_axis_type = 'datetime', sizing_mode = 'scale_width', title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1
hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left = "Start", right = "End", bottom = 0, top = 1, color = "green", source = cds)

output_file("start_time_graph.html")
print("plotting.py data")
show(p)





#Original code from video:
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") #The datetime values are converted to strings.
#Those strings are then put in the df["Start"] column.
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S") #The datetime values are converted into strings and then placed in the df["End"] column.

cds = ColumnDataSource(df) #This converts the df into a format that can be used by Bokeh for plotting.

p = figure(x_axis_type = 'datetime', height = 100, width = 500, sizing_mode = "scale_width", title = "Motion Graph")
p.yaxis.minor_tick_line_color = None #This is used to hide the minor tick marks on the y-axis of the Bokeh plot.
p.ygrid[0].ticker.desired_num_ticks = 1 #Sets amount of ticks in y-axis to 1, and is usually used for grids.
#If you want to set the amount of ticks to 1 on a single y-axis, use: p.ygrid.ticker = [0,1].
#Or: p.yaxis.ticker.desired_num_ticks = 1.

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
#tooltips parameter has two tuples: ("Start", "@Start_string") and ("End", "@End_string").
p.add_tools(hover)

q = p.quad(left = "Start", right = "End", bottom = 0, top = 1, color = "green", source = cds)

output_file("Start_time_graph.html")
print("plotting.py data")
show(p)