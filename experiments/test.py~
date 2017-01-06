from plotly.graph_objs import Bar,Layout,Scatter, Box, Annotation,Marker,Font,XAxis,YAxis
from datetime import datetime
import plotly
import shutil
import random

def plot():
    filename="templates/viz.html"
    x_vals = [random.randint(0,1000) for _ in range(20)]
    y_vals = [random.randint(0,1000) for _ in range(20)]
        
    plotly.offline.plot({
        "data":[Scatter(x=x_vals,y=y_vals)],
        "layout":Layout(
            title="Time Series"
        )
    },auto_open=False)
    shutil.move("temp-plot.html",filename)

if __name__ == '__main__':
    plot()
