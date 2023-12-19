from sys import stdin

def directions_to_turn_character(previous, current):
    mapping = {
        "U": {
            "L": "┐",
            "R": "┌",
            "U": "│",
            "D": "│"
        },
        "D": {
            "L": "┘",
            "R": "└",
            "U": "│",
            "D": "│"
        },
        "L": {
            "U": "└",
            "D": "┌",
            "L": "─",
            "R": "─"
        },
        "R": {
            "U": "┘",
            "D": "┐",
            "L": "─",
            "R": "─"
        }
    }

    return mapping[previous][current]

def digging_plan_size_and_starting_position(digging_plan):
    current_position = (0, 0)
    max_i = max_j= 0
    min_i = min_j = 0

    for direction, length, _ in digging_plan:
        if direction == "U":
            current_position = (current_position[0] - length, current_position[1])
        elif direction == "D":
            current_position = (current_position[0] + length, current_position[1])
        elif direction == "L":
            current_position = (current_position[0], current_position[1] - length)
        elif direction == "R":
            current_position = (current_position[0], current_position[1] + length)
        
        max_i = max(max_i, current_position[0])
        max_j = max(max_j, current_position[1])
        
        min_i = min(min_i, current_position[0])
        min_j = min(min_j, current_position[1])
    
    return (max_i - min_i + 1, max_j - min_j + 1), (-min_i, -min_j)

def count_intersections(diagram, i, j):
    intersections = 0

    remaining_row = diagram[i][j+1:]

    last = None
    for c in remaining_row:
        if last is None:
            if c == "│":
                intersections += 1
            elif c == "┌" or c == "└":
                intersections += 1
                last = c
            # other characters ignored
        else:
            if c == "┐":
                if last == "└":
                    # this counts as only one intersection
                    # already summed before
                    last = None
                else:
                    # this counts as 2 intersections
                    intersections += 1
                    last = None
            elif c == "┘":
                if last == "┌":
                    # this counts as only one intersection
                    # already summed before
                    last = None
                else:
                    # this counts as 2 intersections
                    intersections += 1
                    last = None
            # the other possible case "-" is ignored
    
    return intersections

digging_plan = []

i = j = 0

for line in (l.strip() for l in stdin):
    direction, length, color = line.split(" ")
    digging_plan.append((direction, int(length), color))

    if direction == "U":
        i -= int(length)
    elif direction == "D":
        i += int(length)
    elif direction == "L":
        j -= int(length)
    else:
        j += int(length)

dps, sp = digging_plan_size_and_starting_position(digging_plan)

border = [["." for _ in range(dps[1])] for _ in range(dps[0])]

current_i, current_j = sp

for previous, current in zip([digging_plan[-1]] + digging_plan[:-1], digging_plan):
    previous_direction = previous[0]
    current_direction, current_length, current_color = current

    border[current_i][current_j] = directions_to_turn_character(previous_direction, current_direction)

    if current_direction == "U":
        for i in range(current_i - 1, current_i - current_length, -1):
            # replace characters EXCLUDING FINAL TURN
            border[i][current_j] = "│"
        current_i -= current_length
    elif current_direction == "D":
        for i in range(current_i + 1, current_i + current_length):
            border[i][current_j] = "│"
        current_i += current_length
    elif current_direction == "L":
        for j in range(current_j - 1, current_j - current_length, -1):
            border[current_i][j] = "─"
        current_j -= current_length
    else:
        for j in range(current_j + 1, current_j + current_length):
            border[current_i][j] = "─"
        current_j += current_length
    
area = 0
is_inside = [[False for _ in range(dps[1])] for _ in range(dps[0])]
for i, row in enumerate(border):
    for j, c in enumerate(row):
        if c == ".":
            intersections = count_intersections(border, i, j)

            if intersections % 2 == 1:
                area += 1
                is_inside[i][j] = True

area += sum(1 for row in border for c in row if c != ".")

#print("\n".join(["".join("#" if is_inside[i][j] else c for j, c in enumerate(l)) for i, l in enumerate(border)]))
print(area)
