#Demo
#This is from the Justpy website tutorial on how to make a webpage
#Make sure when creating a webpage, there is a file in the same directory called "justpy.env"
#If there is no such file, the code will not work
#This demo creates a webpage, and in this webpage, there is a bar that says "Hello! Click me"
#If you click the bar, it will show how many times you have clicked on it in the bar itself, switching from the first phrase to "I've been clicked x times"
'''import justpy as jp

def hello_world():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

jp.justpy(hello_world)'''


import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("reviews2.csv", parse_dates = ["Timestamp"])

#to get the code for a specific graph from highcharts, follow these steps:
    #search up highcharts doc
    #click on Highcharts Documentation | Highcharts
    #select "Chart and series types" and find the graph you want to use
    #copy and paste into your code
#in this case, I used the spline chart and copied from the first to last curly bracket
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude',
        align: 'center'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model',
        align: 'center'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]

    }]
}
"""

def app():
    webpage = jp.QuasarPage() #creates the webpage
    heading1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    #makes heading more modern, gives it a bigger font, centers it, and creates a space between the text and the top of the webpage
    #to find fonts, styles, etc, search "quasar style" and click on the "Stylus Variables | Quasar Framework" webpage
    #this should show you different styles and identities that you can use for your webpage
    paragraph1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis") #creates a paragraph
    highchart = jp.HighCharts(a=webpage, options = chart_def) #calls the Javascript code for the spline chart
    #in the line above, it takes the chart_def string and reads it as a dictionary instead because of the curly brackets.
    #print(type(highchart.options)) #shows what class highchart.options is, which is a dictionary that also allows you to access the keys of that dictionary
    #by accessing those keys, you can print out the different keys or change the names or data of those keys, like this:
    highchart.options.title.text = "Average Rating by Day" #changes the title
    #x = [3, 6, 8]
    #y = [4, 7, 9]
    #highchart.options.series[0].data = list(zip(x, y)) #changes the series


    return webpage

jp.justpy(app) #calls app() function
#justpy() is a function that takes care of calling other functions
#when making updates to the code, you will have to stop it from running in the terminal by using Ctrl + C

