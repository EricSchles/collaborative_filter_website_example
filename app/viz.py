import plotly
from plotly.graph_objs import Bar,Layout,Scatter, Box, Annotation,Marker,Font,XAxis,YAxis
from app.models import * 
import shutil

def languages():
    filename = "app/templates/language_frequency.html"
    langs = Languages.query.all()
    lang_dict = {}
    for lang in langs:
        if lang.language not in lang_dict.keys():
            lang_dict[lang.language] = 1
        else:
            lang_dict[lang.language] += 1
        
    x_vals = list(lang_dict.keys()) 
    y_vals = [lang_dict[key] for key in lang_dict.keys()]
        
    plotly.offline.plot({
        "data":[Bar(x=x_vals,y=y_vals)],
        "layout":Layout(
            title="Frequency of languages"
        )
    },auto_open=False)
    shutil.move("temp-plot.html",filename)
