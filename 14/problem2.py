from sys import stdin
import numpy as np

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

def rocks_to_string(rocks):
    return "\n".join("".join(str(c) for c in row) for row in rocks)

def string_to_rocks(string):
    return np.array([[int(c) for c in row] for row in string.split("\n")])

rocks = []
for line in (l.strip() for l in stdin):
    rocks.append(list(line))

rocks = np.array(rocks)
# Operations are calculated by rows, so we transpose
rocks = rocks.transpose()

# Keep track of states to detect loops
reached_states = []
number_cycles = 10**9
loop_start = loop_end = None
for i in range(number_cycles):
    # Check state at the beginning of each spin cycle
    state = rocks_to_string(rocks)
    if state in reached_states:
        # Found this state before, so we have a loop
        loop_start = reached_states.index(state)
        loop_end = i
        break
    else:
        reached_states.append(state)
    
    # Shift north
    rocks = shift_rocks_left(rocks)

    # Shift west
    rocks = np.rot90(rocks, k=1)
    rocks = shift_rocks_left(rocks)

    # Shift south
    rocks = np.rot90(rocks, k=1)
    rocks = shift_rocks_left(rocks)

    # Shift east
    rocks = np.rot90(rocks, k=1)
    rocks = shift_rocks_left(rocks)

    # Back to original orientation
    rocks = np.rot90(rocks, k=1)

if loop_start is not None:
    # Found a loop. Realistically this will always happen, else the previous
    # for loop would not end.
    loop_length = loop_end - loop_start
    loop_index = (number_cycles - loop_start) % loop_length
    state_index = loop_start + loop_index
    rocks = string_to_rocks(reached_states[state_index])

load = get_load_left_beams(rocks)

# If we wanted to print the state of the rocks they should be transposed back

print(load)
