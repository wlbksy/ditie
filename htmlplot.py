#!/usr/bin/env python3

from bokeh.plotting import figure, output_file, save, ColumnDataSource
from bokeh.models import HoverTool, PrintfTickFormatter
import pandas as pd
import numpy as np


def cartesianProduct(df, city):
    feature_label = df.columns
    len_feature_label = len(feature_label)
    for i in range(1, len_feature_label):
        for j in range(1, len_feature_label):
            xlabel = feature_label[i]
            ylabel = feature_label[j]
            render(df, xlabel, ylabel, city)


def render(df, xlabel, ylabel, city):
    output_file(
        "./html/{}_{}_{}.html".format(city, xlabel, ylabel),
        "{}/{}".format(ylabel, xlabel),
    )

    hover = HoverTool(
        tooltips=[("站名", "@desc"), (xlabel, "exp(@x)"), (ylabel, "exp(@y)")]
    )

    source = ColumnDataSource(
        data=dict(x=df[xlabel].map(np.log), y=df[ylabel].map(np.log), desc=df["index"])
    )

    p = figure(
        plot_width=1000,
        plot_height=680,
        tools=["box_zoom, wheel_zoom, reset", hover],
        title=ylabel + "/" + xlabel,
    )

    p.xaxis[0].formatter = PrintfTickFormatter(format="exp(%0.1f )")
    p.yaxis[0].formatter = PrintfTickFormatter(format="exp(%0.1f )")

    p.xaxis.axis_label = xlabel
    p.yaxis.axis_label = ylabel
    p.circle(
        "x",
        "y",
        source=source,
        fill_color="navy",
        hover_fill_color="firebrick",
        fill_alpha=0.05,
        hover_alpha=0.3,
        size=5,
    )
    p.background_fill_color = "beige"
    p.background_fill_alpha = 0.5
    save(p)


df = pd.read_csv("beijing.all.csv")
cartesianProduct(df, "beijing")
