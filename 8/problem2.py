from sys import stdin
from itertools import cycle
import re
from math import lcm

directions = input()

input() # skip blank line

nodes = {}

starting_nodes = []

for line in (l.strip() for l in stdin):
    node, left, right = re.findall(r"([A-Z0-9]{3})", line)
    nodes[node] = (left, right)

    if node[-1] == "A":
        starting_nodes.append(node)

direction_index = {"L": 0, "R": 1}

periodicities = []
for node in starting_nodes:
    for step, d in enumerate(cycle(directions), start=1):
        node = nodes[node][direction_index[d]]
        if node[-1] == "Z":
            periodicities.append(step)
            break

print(lcm(*periodicities))