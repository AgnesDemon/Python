import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates= ["Timestamp"])
share = data.groupby(["Course Name"])["Rating"].count()

chart_definition = """
{
  chart: {
    type: 'pie'
  },
  title: {
    text: 'Egg Yolk Composition'
  },
  tooltip: {
    valueSuffix: '%'
  },
  subtitle: {
    text:
    'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" target="_default">MDPI</a>'
  },
  plotOptions: {
    series: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: [{
        enabled: true,
        distance: 20
      }, {
        enabled: true,
        distance: -40,
        format: '{point.percentage:.1f}%',
        style: {
          fontSize: '1.2em',
          textOutline: 'none',
          opacity: 0.7
        },
        filter: {
          operator: '>',
          property: 'percentage',
          value: 10
        }
      }]
    }
  },
  series: [
    {
      name: 'Percentage',
      colorByPoint: true,
      data: [
        {
          name: 'Water',
          y: 55.02
        },
        {
          name: 'Fat',
          sliced: true,
          selected: true,
          y: 26.71
        },
        {
          name: 'Carbohydrates',
          y: 1.09
        },
        {
          name: 'Protein',
          y: 15.5
        },
        {
          name: 'Ash',
          y: 1.68
        }
      ]
    }
  ]
}
"""

def app():
    webpage = jp.QuasarPage()
    heading1 = jp.QDiv(a=webpage, text= "Analysis of Course Reviews", classes= "text-h3 text-center q-pa-md")
    paragraph1 = jp.QDiv(a=webpage, text = "This pie chart represents the course review analysis")

    highchart = jp.HighCharts(a=webpage, options = chart_definition)
    highchart.options.title.text = "Reviews Pie Chart"
    highchart_data = [{"name": v1, "y": v2} for v1, v2 in zip(share.index, share)]
    highchart.options.series[0].data = highchart_data #the [0] helps us access the dictionary in the json code
    #allows us to access the data key


    return webpage

jp.justpy(app)
