import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
data2 = data.drop(["Comment", "Timestamp"], axis=1)
#print(data2.values.tolist())
month_average_crs = data2.groupby(["Month", "Course Name"])["Rating"].mean().unstack #can use count() or mean()
print(type(month_average_crs)) #reveals that month_average_crs is a class method
print(month_average_crs)
#seems that reviews.csv works and the other names in Column name don't cause a problem
#seems that I can also use .groupby() and .mean() without a problem with reviews.csv

#print(month_average_crs.values.tolist())

chart_definition = """
{
  chart: {
    type: 'areaspline'
  },
  title: {
    text: 'Moose and deer hunting in Norway, 2000 - 2021',
    align: 'left'
  },
  subtitle: {
    text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>',
    align: 'left'
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    verticalAlign: 'top',
    x: 120,
    y: 70,
    floating: true,
    borderWidth: 1,
    backgroundColor:
       || '#FFFFFF'
  },
  xAxis: {
    plotBands: [{ // Highlight the two last years
      from: 2019,
      to: 2020,
      color: 'rgba(68, 170, 213, .2)'
    }]
  },
  yAxis: {
    title: {
      text: 'Quantity'
    }
  },
  tooltip: {
    shared: true,
    headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
  },
  credits: {
    enabled: false
  },
  plotOptions: {
    series: {
      pointStart: 2000
    },
    areaspline: {
      fillOpacity: 0.5
    }
  },
  series: [{
    name: 'Moose',
    data:
      [
        38000,
        37300,
        37892,
        38564,
        36770,
        36026,
        34978,
        35657,
        35620,
        35971,
        36409,
        36435,
        34643,
        34956,
        33199,
        31136,
        30835,
        31611,
        30666,
        30319,
        31766
      ]
  }, {
    name: 'Deer',
    data:
      [
        22534,
        23599,
        24533,
        25195,
        25896,
        27635,
        29173,
        32646,
        35686,
        37709,
        39143,
        36829,
        35031,
        36202,
        35140,
        33718,
        37773,
        42556,
        43820,
        46445,
        50048
      ]
  }]
}
"""

def app():
    webpage = jp.QuasarPage()
    heading1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    paragraph1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis")

    highchart = jp.HighCharts(a=webpage, options=chart_definition)
    #changing names and values in json code:
    highchart.options.chart.type = "spline" #takes off the filled in/colored part of the chart
    highchart.options.title.text = "Average Rating of Course Reviews"
    highchart.options.title.align = "center"
    highchart.options.subtitle.align = "center"

    #highchart.options.xAxis.categories = list(month_average_crs.index) #problem starts here
    #month_average_crs has no attribute to .index
    #highchart_data = [{"name": v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    #highchart.options.series = highchart_data

    #highchart.options.xAxis.categories = month_average_crs
    #highchart_data = [{"name": v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    #highchart.options.series = highchart_data

    return webpage

jp.justpy(app)


#Highcharts.defaultOptions.legend.backgroundColor
#Remember to place this line in front of the two lines "||" before #FFFFFF