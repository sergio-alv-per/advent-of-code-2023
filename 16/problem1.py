from sys import stdin

laser_map = [list(l.strip()) for l in stdin.readlines()]

laser_passed_through_direction = [[set() for _ in range(len(laser_map[0]))] for _ in range(len(laser_map))]

laser_queue = [(0, 0, "R")]

while laser_queue:
    i, j, direction = laser_queue.pop(0)

    if i < 0 or i >= len(laser_map) or j < 0 or j >= len(laser_map[0]):
        # out of bound
        continue
    if direction in laser_passed_through_direction[i][j]:
        # already processed this laser before
        continue
    else:
        laser_passed_through_direction[i][j].add(direction)
    
    # Possible cells: . / \ | -
    cell_type = laser_map[i][j]

    if cell_type == ".":
        # empty space
        if direction == "R":
            laser_queue.append((i, j+1, direction))
        elif direction == "L":
            laser_queue.append((i, j-1, direction))
        elif direction == "U":
            laser_queue.append((i-1, j, direction))
        elif direction == "D":
            laser_queue.append((i+1, j, direction))
    elif cell_type == "/":
        if direction == "R":
            laser_queue.append((i-1, j, "U"))
        elif direction == "L":
            laser_queue.append((i+1, j, "D"))
        elif direction == "U":
            laser_queue.append((i, j+1, "R"))
        elif direction == "D":
            laser_queue.append((i, j-1, "L"))
    elif cell_type == "\\":
        if direction == "R":
            laser_queue.append((i+1, j, "D"))
        elif direction == "L":
            laser_queue.append((i-1, j, "U"))
        elif direction == "U":
            laser_queue.append((i, j-1, "L"))
        elif direction == "D":
            laser_queue.append((i, j+1, "R"))
    elif cell_type == "|":
        if direction == "R" or direction == "L":
            laser_queue.append((i-1, j, "U"))
            laser_queue.append((i+1, j, "D"))
        elif direction == "U":
            laser_queue.append((i-1, j, "U"))
        elif direction == "D":
            laser_queue.append((i+1, j, "D"))
    elif cell_type == "-":
        if direction == "R":
            laser_queue.append((i, j+1, "R"))
        elif direction == "L":
            laser_queue.append((i, j-1, "L"))
        elif direction == "U" or direction == "D":
            laser_queue.append((i, j-1, "L"))
            laser_queue.append((i, j+1, "R"))

print(sum(sum(1 for s in row if s) for row in laser_passed_through_direction))