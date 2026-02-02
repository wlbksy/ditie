#!/usr/bin/env python3

import json

import networkx as nx
import numpy as np
import pandas as pd

#######################################


def get_graph(json_fn):
    d = json.load(open(json_fn, "r"))

    G = nx.DiGraph()

    for line_no in d["valid_lines"]:
        line = d[line_no]
        G.add_node(line[0])
        for i in range(1, len(line)):
            j = i - 1
            G.add_node(line[i])
            G.add_edge(line[i], line[j])
            G.add_edge(line[j], line[i])

    for line_no in d["loops"]:
        cyc_line = d[line_no]
        G.add_edge(cyc_line[-1], cyc_line[0])
        G.add_edge(cyc_line[0], cyc_line[-1])
    UG = nx.Graph(G)

    return UG


def calc_centrality(ug):
    #########################################
    dc = nx.degree_centrality(ug)
    ec = nx.eigenvector_centrality_numpy(ug)
    kc = nx.katz_centrality_numpy(ug)
    cc = nx.closeness_centrality(ug)
    ic = nx.current_flow_closeness_centrality(ug, solver="full")
    bc = nx.betweenness_centrality(ug)
    cfbc = nx.current_flow_betweenness_centrality(ug)
    cbc = nx.communicability_betweenness_centrality(ug)
    lc = nx.load_centrality(ug)
    sc = nx.subgraph_centrality(ug)
    hc = nx.harmonic_centrality(ug)
    soc = nx.second_order_centrality(ug)

    stations = list(ug.nodes())

    station_map = dict()

    for i, station in enumerate(ug.nodes()):
        station_map[station] = i

    feature_list = [
        ["degree", dc],
        ["eigenvector", ec],
        ["katz", kc],
        ["closeness", cc],
        ["information", ic],
        ["betweenness", bc],
        ["currentFlowBetweenness", cfbc],
        ["communicabilityBetweenness", cbc],
        ["load", lc],
        ["subgraph", sc],
        ["harmonic", hc],
        ["secondOrder", soc],
    ]

    features = [i[1] for i in feature_list]
    features_name = [i[0] for i in feature_list]

    rows = len(stations)
    cols = len(features)
    F = np.zeros((rows, cols))

    for j in range(cols):
        for i in features[j].keys():
            row_idx = station_map[i]
            F[row_idx, j] = features[j][i]

    df = pd.DataFrame(F, index=stations, columns=features_name).reset_index()
    df.to_csv("./data/beijing.centrality.csv", index=False)


ug = get_graph("./data/beijing.json")
calc_centrality(ug)
