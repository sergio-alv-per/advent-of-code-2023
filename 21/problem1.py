from sys import stdin
from functools import cache

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
            if 0 <= i + di < len(rocks_map) and 0 <= j + dj < len(rocks_map[0]) and rocks_map[i + di][j + dj] != "#":
                next_squares.add((i + di, j + dj))

        return next_squares

@cache
def reachable(i, j, steps):
    ns = next_squares(i, j)
    if steps == 1:
        return ns
    else:
        union = set()
        for square in ns:
            union |= reachable(*square, steps-1)
        
        return union

for i, row in enumerate(rocks_map):
    for j, c in enumerate(row):
        if c == "S":
            start = (i, j)

print(len(reachable(*start, 64)))


