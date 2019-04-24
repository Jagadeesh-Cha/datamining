import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy as np
G=nx.Graph() 
G = nx.read_edgelist('subgraph6.txt', nodetype = int)
n = len(G.nodes())

print("no of nodes in graph:"+str(n))
t = int(n/100)
N=list(G.nodes())
W = list(G.nodes())
H1=[]
H2=[]
D=[]
DDD=[]
DD=[]
index=0
''' Finding the H1 indeces of the nodes of graph'''
for i in range(n):
      P = list(G.neighbors(N[i]))
      for j in range(len(P)):
            D.append(G.degree(P[j]))
      D.sort()
      myset=set(D)
      DDD=list(myset)
      
      for b in range(len(DDD)):
      
            DD.append(D.count(DDD[b])) 
      for h in range(len(DDD)):
            if( DD[h] >= DDD[h] ):index=DDD[h]	
      H1.append(index)
      D=[]
      DD=[]
      DDD=[]
      index = 0
    
''' Finding the H2 indeces of the nodes of graph '''

E=[]
EE=[]
EEE=[]
for i in range(n):
      R = list(G.neighbors(N[i]))
      for j in range(len(R)):
            E.append(H1[N.index(R[j])])
      E.sort()
      mset=set(E)
      EEE=list(mset)
      for k in range(len(EEE)):
            EE.append(E.count(EEE[k])) 
      for h in range(len(EEE)):
            if( EE[h] >= EEE[h] ):index=EEE[h]	
      H2.append(index)
      E=[]
      EE=[]
      EEE=[]
      index = 0
q=0
print("no of different H2 indeces in the graph are : "+str(len(list(set(H2)))))
#walk
max_encountered_list = []
walk=[]
shell_list=[]
shell_set_list=[]
distint_shell_list=[]
F=[]
f=0
no_of_steps=[]
H2_1=[]
H2_2=[]
#k = len(buckets)
#periphery nodes:
for i in range(len(G.nodes())):
      if(H2[i] == min(H2)):H2_1.append(N[i])

maximum = max(H2)
for i in range(len(G.nodes())):
      if(H2[i] == max(H2)):H2_2.append(N[i])

print(H2_2)