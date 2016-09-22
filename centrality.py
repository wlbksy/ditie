#!/usr/bin/env python3

import networkx as nx
import pandas as pd
import numpy as np

from beijing import *
#######################################

def calc_centrality(city):
    G = nx.DiGraph()

    for line in all_lines:
        G.add_node(line[0])
        for i in range(1, len(line)):
            j = i-1
            G.add_node(line[i])
            G.add_edge(line[i],line[j])
            G.add_edge(line[j],line[i])
    #######################################
    for cyc_line in cyclic_lines:
        G.add_edge(cyc_line[-1],cyc_line[0])
        G.add_edge(cyc_line[0],cyc_line[-1])
    UG = nx.Graph(G)

    #########################################
    dc = nx.degree_centrality(UG)
    cc = nx.closeness_centrality(UG)
    bc = nx.betweenness_centrality(UG)
    ec = nx.eigenvector_centrality_numpy(UG)

    stations = UG.nodes()

    features = [dc, cc, bc, ec]
    rows = len(stations)
    cols = len(features)
    F = np.zeros((rows, cols))

    for j in range(cols):
        for i in features[j].keys():
            row_idx = stations.index(i)
            F[row_idx, j] = features[j][i]

    features_name= ['degree', 'closeness', 'betweenness', 'eigenvector']
    df = pd.DataFrame(F, index=stations, columns=features_name).reset_index()
    df.to_csv(city+".centrality.csv", index=False)
    df.to_csv(city+".all.csv", index=False)
    ############################################


calc_centrality('beijing')
