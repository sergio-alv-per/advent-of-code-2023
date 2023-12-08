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


diagram = []
for line in (l.strip() for l in stdin):
    diagram.append(make_readable(line))

current_i, current_j = find_start(diagram)
current_direction_1, current_direction_2 = find_starting_directions(diagram, current_i, current_j)

directions = [[current_i, current_j, current_direction_1], [current_i, current_j, current_direction_2]]

steps = 0
while directions:
    i, j, direction = directions.pop(0)
    
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
    
    steps += 1

    if directions[0][:2] == directions[1][:2]:
        break
   

print("\n".join([l for l in diagram]))
print(int(steps/2))