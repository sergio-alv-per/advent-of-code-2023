from sys import stdin
from functools import cache
import numpy as np

# Inspired by https://reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/keao6r4/

rocks_map = []
for line in (l.strip() for l in stdin):
    rocks_map.append(list(line))

@cache
def rocks_map_transported(i, j):
    transported_i = i % len(rocks_map)
    transported_j = j % len(rocks_map[0])

    return rocks_map[transported_i][transported_j]

@cache
def next_squares(i, j):
    if rocks_map_transported(i, j) == "#":
        return set()
    else:
        next_squares = set()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            adjacent_i = i + di
            adjacent_j = j + dj

            if rocks_map_transported(adjacent_i, adjacent_j) != "#":
                next_squares.add((adjacent_i, adjacent_j))

        return next_squares
    
def reachable_in_steps(start_i, start_j, start_steps):
    reachable = set()
    visited = set()
    queue = [(start_i, start_j, start_steps)]
    
    while queue:
        i, j, steps = queue.pop()

        if (i, j, steps) in visited:
            continue
        else:
            visited.add((i, j, steps))

        if steps == 0:
            reachable.add((i, j))
        else:
            queue.extend((next_i, next_j, steps-1) for (next_i, next_j) in next_squares(i, j))
    
    return reachable

def find_replace_S(rocks_map):
    for i, row in enumerate(rocks_map):
        for j, c in enumerate(row):
            if c == "S":
                row[j] = "."
                return (i, j)

start = find_replace_S(rocks_map)

n_reachable_tiles = []
for i in range(3):
    N = 65 + 131*i
    print(f"Calculating for {N}...")
    R = reachable_in_steps(*start, N)
    n_reachable_tiles.append(len(R))
    print(len(R))

# 26501365 = 202300 * 131 + 65
# We have the value of the polynomial for 65, 65 + 131, 65 + 2*131
# Taking g(t) = 65 + 131*t, we have the values of the polynomial for g(0), g(1), g(2)
# Defining h = p.g we have the values of h for 0, 1, 2 
h_coefficients = np.polyfit([0, 1, 2], n_reachable_tiles, 2)

def h(t):
    return round(np.polyval(h_coefficients, t))

# g(202300) = 26501365, so to get the value of p(26501365) we evaluate h(202300)
print(h(202300))



