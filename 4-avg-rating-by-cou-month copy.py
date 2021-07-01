from ssl import Options
import justpy as jp
from justpy.htmlcomponents import Option
from pandas.core.dtypes.common import classes

import pandas as pd
from pytz import utc 


data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crn = data.groupby(['month', 'Course Name'])['Rating'].mean().unstack()

chart_desc = """
{
  chart: {
    type: 'spline'
  },
  title: {
    text: 'Average fruit consumption during one week'
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    verticalAlign: 'top',
    x: 150,
    y: 100,
    floating: false,
    borderWidth: 1,
    backgroundColor:
      '#FFFFFF'
  },
  xAxis: {
    categories: [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday'
    ],
    plotBands: [{ // visualize the weekend
      from: 4.5,
      to: 6.5,
      color: 'rgba(68, 170, 213, .2)'
    }]
  },
  yAxis: {
    title: {
      text: 'Fruit units'
    }
  },
  tooltip: {
    shared: true,
    valueSuffix: ' units'
  },
  credits: {
    enabled: false
  },
  plotOptions: {
    areaspline: {
      fillOpacity: 0.5
    }
  },
  series: [{
    name: 'John',
    data: [3, 4, 3, 5, 4, 10, 12]
  }, {
    name: 'Jane',
    data: [1, 3, 4, 3, 3, 5, 4]
  }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Riviews", classes="text-h3 text-center")    
    p1 =  jp.QDiv(a=wp, text="This graph represent course review analysis", classes="text-h3 text-center")
    
    hc = jp.HighCharts(a=wp, options=chart_desc)
    # hc.options.title.text = "Average Rating by Month"
    # hc.options.series[0].name = "Rating"

    hc.options.xAxis.categories = list(month_average_crn.index)

    hc_data = [
        {'name': v1, 'data':[v2 for v2 in month_average_crn[v1]]} for v1 in month_average_crn.columns
    ]
    hc.options.series = hc_data 

    # hc.options.series[0].data = list(zip(day_average.index, day_average['Rating']))



    return wp

jp.justpy(app)