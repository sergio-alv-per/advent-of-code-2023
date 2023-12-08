from sys import stdin
from itertools import cycle
import re

directions = input()

input() # skip blank line

nodes = {}

for line in (l.strip() for l in stdin):
    node, left, right = re.findall(r"([A-Z]{3})", line)
    nodes[node] = (left, right)

current_node = "AAA"

# Brute force solution
directions = [0 if d == "L" else 1 for d in directions]
for step, d in enumerate(cycle(directions), start=1):   
    current_node = nodes[current_node][d]
    if current_node == "ZZZ":
        print(step)
        break