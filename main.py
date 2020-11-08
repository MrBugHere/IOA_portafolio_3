import networkx as nx
from casos.c100x500 import data

graph = nx.Graph()
graph.add_weighted_edges_from(data)
src = 1
trget = 100
print(nx.dijkstra_path(graph, src, trget))
# print ()