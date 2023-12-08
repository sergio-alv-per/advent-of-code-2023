from sys import stdin

def make_readable(line):
    line = line.replace("L", "└")
    line = line.replace("J", "┘")
    line = line.replace("F", "┌")
    line = line.replace("7", "┐")
    line = line.replace("|", "│")
    line = line.replace("-", "─")
    line = line.replace(".", " ")
    line = line.replace("S", "●")
    return line

def find_start(diagram):
    for i, row in enumerate(diagram):
        if "●" in row:
            return i, row.index("●")

def find_starting_directions(diagram, i, j):
    directions = []
    if i > 0 and diagram[i-1][j] in "│┐┌":
        directions.append("U") # Up
    if i < len(diagram)-1 and diagram[i+1][j] in "│└┘":
        directions.append("D") # Down
    if j > 0 and diagram[i][j-1] in "┌└─":
        directions.append("L") # Left
    if j < len(diagram[i])-1 and diagram[i][j+1] in "─┐┘":
        directions.append("R") # Right
    return directions

def next_from_direction(i, j, direction):
    if direction == "U":
        return i-1, j
    elif direction == "D":
        return i+1, j
    elif direction == "L":
        return i, j-1
    elif direction == "R":
        return i, j+1

def count_intersections(cleared_diagram, i, j):
    intersections = 0

    remaining_row = cleared_diagram[i][j+1:]

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

def generate_is_tube_matrix(diagram):
    is_tube = [[False for _ in range(len(diagram[0]))] for _ in range(len(diagram))]

    current_i, current_j = find_start(diagram)
    current_direction_1, current_direction_2 = find_starting_directions(diagram, current_i, current_j)

    directions = [[current_i, current_j, current_direction_1], [current_i, current_j, current_direction_2]]

    while directions:
        i, j, direction = directions.pop(0)

        is_tube[i][j] = True
        
        next_i, next_j = next_from_direction(i, j, direction)

        if direction == "U":
            if diagram[next_i][next_j] == "│":
                directions.append([next_i, next_j, "U"])
            elif diagram[next_i][next_j] == "┐":
                directions.append([next_i, next_j, "L"])
            elif diagram[next_i][next_j] == "┌":
                directions.append([next_i, next_j, "R"])
        elif direction == "D":
            if diagram[next_i][next_j] == "│":
                directions.append([next_i, next_j, "D"])
            elif diagram[next_i][next_j] == "┘":
                directions.append([next_i, next_j, "L"])
            elif diagram[next_i][next_j] == "└":
                directions.append([next_i, next_j, "R"])
        elif direction == "L":
            if diagram[next_i][next_j] == "─":
                directions.append([next_i, next_j, "L"])
            elif diagram[next_i][next_j] == "└":
                directions.append([next_i, next_j, "U"])
            elif diagram[next_i][next_j] == "┌":
                directions.append([next_i, next_j, "D"])
        else:
            if diagram[next_i][next_j] == "─":
                directions.append([next_i, next_j, "R"])
            elif diagram[next_i][next_j] == "┘":
                directions.append([next_i, next_j, "U"])
            elif diagram[next_i][next_j] == "┐":
                directions.append([next_i, next_j, "D"])
        
        if directions[0][:2] == directions[1][:2]:
            is_tube[directions[0][0]][directions[0][1]] = True
            break
    
    return is_tube

def generate_cleared_diagram(diagram, is_tube):
    cleared_diagram = [[c if i_t else "·" for c, i_t in zip(row, is_tube_row)] for row, is_tube_row in zip(diagram, is_tube)]
    return cleared_diagram


diagram = []
for line in (l.strip() for l in stdin):
    diagram.append(make_readable(line))

is_tube = generate_is_tube_matrix(diagram)
cleared_diagram = generate_cleared_diagram(diagram, is_tube)

area = 0
is_inside = [[False for _ in range(len(cleared_diagram[0]))] for _ in range(len(cleared_diagram))]

for i, row in enumerate(cleared_diagram):
    for j, c in enumerate(row):
        if not is_tube[i][j]:
            intersections = count_intersections(cleared_diagram, i, j)

            if intersections % 2 == 1:
                area += 1
                is_inside[i][j] = True


diagram_inside_marked = [["I" if ins else c for c, ins in zip(row, inside_row)] for row, inside_row in zip(cleared_diagram, is_inside)]
print("\n".join(["".join(l) for l in diagram_inside_marked]))
print(area)