#To open Jupyter Notebook from terminal, type "jupyter notebook".
#To run something in Jupyter, press Shift + Enter.

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

