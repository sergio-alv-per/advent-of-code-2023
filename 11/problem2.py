from sys import stdin
from itertools import combinations


def manhattan_distance(i1, j1, i2, j2):
    return abs(i2 - i1) + abs(j2 - j1)

def galaxy_distance(i1, j1, i2, j2, empty_rows, empty_columns):
    """To find distances between galaxies, find the number of empty columns and
    rows between them. Then use them as a factor, adding them to the Manhattan
    distance.
    """
    empty_rows_between_galaxies = len([x for x in empty_rows if min(i1, i2) < x < max(i1, i2)])
    empty_columns_between_galaxies = len([x for x in empty_columns if min(j1, j2) < x < max(j1, j2)])

    return manhattan_distance(i1, j1, i2, j2) + (10**6 - 1)*(empty_rows_between_galaxies + empty_columns_between_galaxies)

# Read input
galaxy_map = []
for line in (l.strip() for l in stdin):
    galaxy_map.append(list(line))

# Find empty rows and columns
empty_rows = []
empty_columns = []
for i in range(len(galaxy_map)-1, -1, -1):
    row = galaxy_map[i]
    if all(c == "." for c in row):
        empty_rows.append(i)

for j in range(len(galaxy_map[0])-1, -1, -1):
    if all(galaxy_map[i][j] == "." for i in range(len(galaxy_map))):
        empty_columns.append(j)

# Find galaxies
galaxy_positions = []
for i, row in enumerate(galaxy_map):
    for j, c in enumerate(row):
        if c == "#":
            galaxy_positions.append((i, j))

# Iterate over pairs of galaxies and sum distances
distance_sum = 0
for pos1, pos2 in combinations(galaxy_positions, 2):
    distance_sum += galaxy_distance(*pos1, *pos2, empty_rows, empty_columns)

print(distance_sum)