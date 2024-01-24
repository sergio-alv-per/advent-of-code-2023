from sys import stdin
from collections import defaultdict
import networkx as nx
import argparse

# Execute with pairs of nodes to remove as arguments:
# python3 problem1-2.py gpz,prk lsk,rfq zhg,qdv
parser = argparse.ArgumentParser()
parser.add_argument("removed_edges", nargs="*")
args = parser.parse_args()

removed_edges = set()
for pair in args.removed_edges:
    removed_edges.add(tuple(pair.split(",")))

graph = defaultdict(set)

for l in (l.strip() for l in stdin):
    origin, destinations = l.split(": ")
    destinations = destinations.split(" ")
    
    for d in destinations:
        graph[origin].add(d)
        graph[d].add(origin)

for p1, p2 in removed_edges:
    graph[p1].remove(p2)
    graph[p2].remove(p1)

G = nx.Graph(graph)

C1, C2 = nx.connected_components(G)

print(f"Nodes in connected componets: {len(C1)}, {len(C2)}")
print(f"Product of nodes in connected components: {len(C1) * len(C2)}")

