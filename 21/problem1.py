from sys import stdin
from functools import cache

# Inspired by https://reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/keao6r4/

rocks_map = []
for line in (l.strip() for l in stdin):
    rocks_map.append(list(line))
@cache
def next_squares(i, j):
    if rocks_map[i][j] == "#":
        return set()
    else:
        next_squares = set()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            adjacent_i = i + di
            adjacent_j = j + dj

            if rocks_map[adjacent_i][adjacent_j] != "#":
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

print(len(reachable_in_steps(*start, 64)))