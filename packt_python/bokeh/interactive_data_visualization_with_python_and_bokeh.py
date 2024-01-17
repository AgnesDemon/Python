#To open Jupyter Notebook from terminal, type "jupyter notebook".
#To run something in Jupyter, press Shift + Enter.
#To delete a box, click out of the box so it isn't highlighted anymore. Then press "d" twice.
#Don't forget about assignments! You can access them by going to the "Resources" folder and finding the folder for the chapter you are on.


#making a basic bokeh line graph
    #from bokeh.plotting import figure
    #from bokeh.io import output_file, show
#preparing data
    #x = [1, 2, 3]
    #y = [6, 7, 8]
#preparing the output file
    #output_file("Line.html")
#creating figure object
    #f = figure()
#creating line plot
    #f.line(x,y)
#writing the plot in the figure object
    #show(f)
#This will take the data from the two lists - x and y - and create a line plot with the data in another window.

#For the sake of this example, say the data.csv file had this data:
    #x,y
    #1,6
    #2,7
    #3,8
    #4,9
    #5,10
#making a basic bokeh line graph
    #from bokeh.plotting import figure
    #from bokeh.io import output_file, show
    #import pandas
#preparing data
    #df = pandas.read_csv("data.csv")
    #x = df["x"]
    #y = df["y"]
#preparing the output file
    #output_file("Line_from_csv.html")
#creating figure object
    #f = figure()
#creating line plot
    #f.line(x,y)
#writing the plot in the figure object
    #show(f)
#This takes in data from a csv file and uses that data to make a plot line.

#Making a time series graph (THIS METHOD IS NOT WORKING AT THE MOMENT DUE OUTDATED METHODS AND UPDATED DATA)
    #from bokeh.plotting import figure, output_file, show
    #import pandas

    #df = pandas.read_csv("link", parse_dates = ["Date"]) 
    #p = figure(width=500, height=250, x_axis_type="datetime", responsive=True) #This is where the error occurs
#To fix the error, change "responsive=True" to sizing_mode="scale_width"
#responsive=True is outdated and no longer in pandas
    #p.line(df["Date"], df["Close"], color="Orange", alpha=0.5)
#alpha controls transparency
    #output_file("Timeseries.html")
    #show(p)

#link 1: http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv
#link 2 (assignment): https://pythonizing.github.io/data/bachelors.csv
#link 3: bokeh.pydata.org/en/latest/docs/user_guide/plotting.html (Page no longer exists. Just go to bokeh.pydata.org)
#link 4 (assignment): https://github.com/pythonizing/data/raw/master/verlegenhuken.xlsx

#This isn't working either
    #from bokeh.plotting import figure, output_file, show
    #import pandas

    #p = figure(plot_width=500, plot_height=400, tools='pan', logo=None) #This line seems to be the problem
#Switch previous line to:
    #p = figure(width=500, height=400, tools='pan')
    #p.toolbar.logo = None
#This will allow code to work again
    #p.title.text = "Cool Data"
    #p.title.text_color = "Gray"
    #p.title.text_font = "times"
    #p.title.text_font_style = "bold"

    #p.xaxis.minor_tick_line_color = None
    #p.yaxis.minor_tick_line_color = None
    #p.xaxis.axis_label = "Date"
    #p.yaxis.axis_label = "Intensity"

    #x = [1,2,3]
    #y = [4,5,6]

    #p.line(x,y)
    #output_file("graph.html")
    #show(p)

#
#