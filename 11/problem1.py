from sys import stdin
from itertools import combinations

def manhattan_distance(x1, y1, x2, y2):
    """Shortest distance in the grid going only in cardinal directions is Manhattan distance."""
    return abs(x2 - x1) + abs(y2 - y1)

# Read input
galaxy_map = []
for line in (l.strip() for l in stdin):
    galaxy_map.append(list(line))

# Duplicate empty rows
for i in range(len(galaxy_map)-1, -1, -1):
    row = galaxy_map[i]
    if all(c == "." for c in row):
        galaxy_map.insert(i, ["."]*len(row))

# Duplicate empty columns
for j in range(len(galaxy_map[0])-1, -1, -1):
    if all(galaxy_map[i][j] == "." for i in range(len(galaxy_map))):
        for i in range(len(galaxy_map)):
            galaxy_map[i].insert(j, ".")

# Find galaxy positions
galaxy_positions = []
for i, row in enumerate(galaxy_map):
    for j, c in enumerate(row):
        if c == "#":
            galaxy_positions.append((i, j))

# Iterate over galaxy pairs, finding ditance between each one
distance_sum = 0
for pos1, pos2 in combinations(galaxy_positions, 2):
    distance_sum += manhattan_distance(*pos1, *pos2)

print(distance_sum)