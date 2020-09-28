#!/usr/bin/env python3

import networkx as nx
import pandas as pd
import numpy as np

from beijing import all_lines, cyclic_lines
from construct_graph import get_graph

#######################################


def calc_centrality():
    UG = get_graph(all_lines, cyclic_lines)

    #########################################
    dc = nx.degree_centrality(UG)
    cc = nx.closeness_centrality(UG)
    bc = nx.betweenness_centrality(UG)
    ec = nx.eigenvector_centrality_numpy(UG)

    stations = list(UG.nodes())

    station_map = dict()

    for i, station in enumerate(UG.nodes()):
        station_map[station] = i

    features = [dc, cc, bc, ec]
    rows = len(stations)
    cols = len(features)
    F = np.zeros((rows, cols))

    for j in range(cols):
        for i in features[j].keys():
            row_idx = station_map[i]
            F[row_idx, j] = features[j][i]

    features_name = ["degree", "closeness", "betweenness", "eigenvector"]
    df = pd.DataFrame(F, index=stations, columns=features_name).reset_index()
    df.to_csv("./data/beijing.centrality.csv", index=False)


calc_centrality()
