import operator
import pandas as pd
from collections import Counter
import networkx as nx

with open("Brightkite_totalCheckins.txt", "r") as f:
    lines = f.readlines()
with open("busy.txt", "w") as f:
    for line in lines:
        if line.split()[-1] == 'ecbfba0ca22411ddb71dfb65ad521832':
            f.write(line)
with open('busy.txt') as f:
   list1 = [int(line.split()[0]) for line in f]
list_set = set(list1)
listu = list(list_set)

G=nx.Graph() 
G = nx.read_edgelist('Brightkite_edges.txt', nodetype = int)
H = G.subgraph(listu)
nx.write_edgelist(H, "subgraph10.edgelist")