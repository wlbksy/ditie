#!/usr/bin/env python3

import networkx as nx
import pandas as pd
import numpy as np
from collections import defaultdict

#######################################
## simulate path for beijing
from beijing import *

#######################################
total_loops = 100000

def calc_centrality():
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

    return UG

def calcSingle(start_node, G, total_loops):
    res = defaultdict(dict)
    for i in G.nodes():
        res[i] = defaultdict(int)

    nodes = G.nodes()
    for loop in range(total_loops):
        nodes_set = set(nodes)
        next_node = start_node
        nodes_set.remove(next_node)
        steps = 1
        bool_continue = True
        while bool_continue:
            set_neighbors = set(G.neighbors(next_node)) & nodes_set
            if set_neighbors:
                next_node = np.random.choice(list(set_neighbors), 1)[0]
                nodes_set.remove(next_node)
                res[next_node][steps] += 1
                steps += 1
            else:
                bool_continue = False
    return res

def calcAll(G, total_loops):
    res = dict()
    for i in G.nodes():
        res[i] = calcSingle(i, G, total_loops)
    return res

def main(G, total_loops):
    result_dict = calcAll(G, total_loops)

    with open('acc_'+str(total_loops)+'.csv', 'w') as f:
        for start_node, v1 in result_dict.items():
            for end_node, v2 in v1.items():
                for h, v3 in v2.items():
                    f.write(start_node+','+end_node+','+str(h)+','+str(v3)+'\n')



G = calc_centrality()

# main(G, total_loops)

##########################################################################
### calculate accessibility for beijing
##########################################################################

denominator = len(G.nodes()) -1

df = pd.read_csv('acc_'+str(total_loops)+'.zip', names=['begin','end','step','nums'], compression='zip')
# df = pd.read_csv('acc_'+str(total_loops)+'.csv', names=['begin','end','step','nums'])

df['p'] = df['nums']/total_loops

df['entropy'] = - df['p'] * np.log(df['p'])

##########################################################################

entropy_df = df.groupby(['begin', 'step'])['entropy'].sum().reset_index()

entropy_df['meanK'] = entropy_df['entropy'].map(np.exp)/denominator

##########################################################################

all_df = entropy_df.groupby(['begin'])['entropy'].sum().reset_index()
all_df.columns = ['begin', 'entropyK']

mean_df = entropy_df.groupby(['begin'])['meanK'].mean().reset_index()

accessibility_df = all_df.merge(mean_df, on=['begin'])

##########################################################################

centrality_df = pd.read_csv('beijing.centrality.csv')

result_df = centrality_df.merge(accessibility_df, left_on=['index'], right_on=['begin'])

del result_df['begin']
result_df.to_csv('beijing.all.'+str(total_loops)+'.csv', index=False)
result_df.to_csv('beijing.all.csv', index=False)

