import matplotlib.pyplot as plt
import networkx as nx
G=nx.Graph() 
pos=nx.spring_layout(G)
G = nx.read_edgelist('subgraph10.txt', nodetype = int)
color_map = []
for node in G:
    if node in [691, 18, 58, 83, 189, 4825, 12069, 61, 159, 881, 1776, 1999, 2038, 324, 22604, 431, 8654, 8775, 8789, 8914, 1578, 55560, 48617, 56503, 6123, 1119, 999, 362, 682, 49072]:
        color_map.append('red')
    else: color_map.append('blue')      
nx.draw(G,node_color = color_map,with_labels = False)
plt.show()