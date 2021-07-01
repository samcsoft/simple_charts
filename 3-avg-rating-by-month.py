from ssl import Options
import justpy as jp
from justpy.htmlcomponents import Option
from pandas.core.dtypes.common import classes

import pandas as pd
from pytz import utc 


data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['month']).mean()
chart_desc = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Timestamp Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
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
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Averaging Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Riviews", classes="text-h3 text-center")    
    # p1 =  jp.QDiv(a=wp, text="This graph represent course review analysis")
    
    hc = jp.HighCharts(a=wp, options=chart_desc)
    hc.options.title.text = "Average Rating by Month"
    hc.options.series[0].name = "Rating"

    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average['Rating'])

    # hc.options.series[0].data = list(zip(day_average.index, day_average['Rating']))



    return wp

jp.justpy(app)