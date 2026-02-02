import numpy as np
import pandas as pd
import plotly.express as px


def cartesianProduct(df, city):
    feature_label = df.columns
    len_feature_label = len(feature_label)
    for i in range(1, len_feature_label):
        for j in range(1, len_feature_label):
            xlabel = feature_label[i]
            ylabel = feature_label[j]
            render(df, xlabel, ylabel, city)


def render(df, xlabel, ylabel, city):
    fig = px.scatter(
        df,
        x=xlabel,
        y=ylabel,
        hover_name="index",
        log_x=True,
        log_y=True,
    )

    fig.update_traces(
        marker_line_width=1,
        marker_size=5,
        marker_color=np.random.randn(len(df)),
    )

    fig.write_html("./html/{}_{}_{}.html".format(city, xlabel, ylabel))


df = pd.read_csv("./data/beijing.centrality.csv")
cartesianProduct(df, "beijing")
