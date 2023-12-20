from sys import stdin
from functools import cache
from collections import defaultdict

def calculate_steps_without_turn(node, adjacent_direction_name):
    if node[2] == adjacent_direction_name:
        return node[3] + 1
    else:
        return 1

@cache
def is_out_of_bounds(position, rows, columns):
    return position[0] < 0 or position[1] < 0 or position[0] >= rows or position[1] >= columns

def neighbours(graph, node):
    neighbours = []

    for adjacent_direction, direction_name in [((0, 1), "E"), ((1, 0), "S"), ((0, -1), "W"), ((-1, 0), "N")]:
        new_position = (node[0] + adjacent_direction[0], node[1] + adjacent_direction[1])

        steps_without_turn = calculate_steps_without_turn(node, direction_name)

        if steps_without_turn > 3 or is_out_of_bounds(new_position, len(graph), len(graph[0])):
            continue

        neighbours.append((*new_position, direction_name, steps_without_turn))
    
    return neighbours

def cost(graph, position_1, position_2):
    return graph[position_2[0]][position_2[1]]


def dijkstra(graph, start_position, end_position):
    distance = defaultdict(lambda: float("inf"))
    previous = {}
    result = []

    start_node = (*start_position, None, 0)

    distance[start_node] = 0

    alive_nodes = set()
    already_visited = set()

    for n in neighbours(graph, (*start_position, "E", 0)):
        alive_nodes.add(n)
        distance[n] = cost(graph, start_position, n)
        previous[n] = start_node

    while alive_nodes:
        u = min(alive_nodes, key=lambda x: distance[x])
        alive_nodes.remove(u)
        already_visited.add(u)

        if u[:2] == end_position:
            break

        for n in neighbours(graph, u):
            if previous[u][:2] == n[:2]:
                # don't go back
                continue

            if n not in already_visited and distance[n] > distance[u] + cost(graph, u, n):
                distance[n] = distance[u] + cost(graph, u, n)
                previous[n] = u
                alive_nodes.add(n)
                

    return distance, previous


cost_map = [[int(c) for c in l.strip()] for l in stdin.readlines()]

start_position = (0, 0)
end = (len(cost_map) - 1, len(cost_map[0]) - 1)

distance, previous = dijkstra(cost_map, start_position, end)

print(min(distance[(end[0], end[1], d, s)] for d in "NESW" for s in range(4)))