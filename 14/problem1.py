from sys import stdin

def transpose(lst):
    return [list(col) for col in zip(*lst)]

def find_last_lower(lst, value):
    for i, v in enumerate(lst):
        if v > value:
            return lst[i - 1]
    return lst[-1]

def shift_rocks_left(rocks):
    for row in rocks:
        steady_rocks = [-1] + [i for i, c in enumerate(row) if c == "#"]
        for i, c in enumerate(row):
            if c == "O":
                last_lower = find_last_lower(steady_rocks, i)
                row[i] = "."
                row[last_lower + 1] = "O"
                steady_rocks.append(last_lower + 1)
                steady_rocks.sort()
    
    return rocks

def get_load_left_beams(rocks):
    load = 0
    for row in rocks:
        for i, c in enumerate(tuple(reversed(row)), start=1):
            if c == "O":
                load += i
    
    return load


rocks = []
for line in (l.strip() for l in stdin):
    rocks.append(list(line))

transposed_rocks = transpose(rocks)
transposed_rocks = shift_rocks_left(transposed_rocks)
load = get_load_left_beams(transposed_rocks)

print(load)
