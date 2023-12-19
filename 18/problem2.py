from sys import stdin

def get_instruction_from_hex(line):
    dir_mapping = "RDLU"
    instruction = line.split(" ")[-1]
    instruction = instruction[2:-1]
    length = int(instruction[:-1], 16)
    direction = int(instruction[-1])
    direction = dir_mapping[direction]
    return direction, length

def get_default_instruction(line):
    direction, length = line.split(" ")[:-1]
    length = int(length)
    return direction, length


current_i = current_j = 0
points = [(current_i, current_j)]
border_pieces = 0

for line in (l.strip() for l in stdin):
    direction, length = get_instruction_from_hex(line)
    #direction, length = get_default_instruction(line)

    current_i += (direction == "D") * length - (direction == "U") * length
    current_j += (direction == "R") * length - (direction == "L") * length
    border_pieces += length
    points.append((current_i, current_j))

# Shoe lace formula
area = 1/2 * sum((p1[1] + p2[1])*(p1[0] - p2[0]) for p1, p2 in zip(points, points[1:]))
area = abs(area)

# Pick's theorem
interior = int(area + 1 - border_pieces/2)

print(interior + border_pieces)
