from sys import stdin
from collections import defaultdict
import networkx as nx
import pyvis as pv

graph = defaultdict(set)

for l in (l.strip() for l in stdin):
    origin, destinations = l.split(": ")
    destinations = destinations.split(" ")
    
    for d in destinations:
        graph[origin].add(d)
        graph[d].add(origin)

G = nx.Graph(graph)

NT = pv.network.Network("800px", "800px")
NT.from_nx(G)

NT.save_graph("~/graph.html")

