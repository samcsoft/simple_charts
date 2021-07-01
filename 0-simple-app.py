import justpy as jp
from pandas.core.dtypes.common import classes
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Riviews", classes="text-h3 text-center")    
    p1 =  jp.QDiv(a=wp, text="This graph represent course review analysis")
    return wp

jp.justpy(app)
    
