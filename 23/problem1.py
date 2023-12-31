from sys import stdin
from collections import namedtuple

Point = namedtuple('Point', ["i", "j"])

def load_labyrinth():
    labyrinth = []

    for line in stdin:
        labyrinth.append(line.strip())

    labyrinth.insert(0, "#" * len(labyrinth[0]))
    labyrinth.append("#" * len(labyrinth[0]))

    return labyrinth

def longest_distance(labyrinth):
    first = Point(1, 1)
    second = Point(2, 1)
    last = Point(len(labyrinth) - 2, len(labyrinth[-1]) - 2)

    open_queue = [(first, second)]

    max_distance = 0

    while open_queue:
        path = open_queue.pop(0)
        current = path[-1]
        previous = path[-2]

        if current in path[:-1]:
            continue

        if current == last:
            if len(path)-1 > max_distance:
                max_distance = len(path)-1
            continue
        
        current_char = labyrinth[current.i][current.j]

        if current_char == ">":
            next_point = Point(current.i, current.j + 1)
            open_queue.append(path + (next_point,))
        elif current_char == "v":
            next_point = Point(current.i + 1, current.j)
            open_queue.append(path + (next_point,))
        elif current_char == ".":
            right = Point(current.i, current.j + 1)
            if right != previous and labyrinth[right.i][right.j] in ".>":
                open_queue.append(path + (right,))
            
            left = Point(current.i, current.j - 1)
            if left != previous and labyrinth[left.i][left.j] == ".":
                open_queue.append(path + (left,))
                
            up = Point(current.i - 1, current.j)
            if up != previous and labyrinth[up.i][up.j] == ".":
                open_queue.append(path + (up,))
            
            down = Point(current.i + 1, current.j)
            if down != previous and labyrinth[down.i][down.j] in ".v":
                open_queue.append(path + (down,))

    return max_distance

print(longest_distance(load_labyrinth()))