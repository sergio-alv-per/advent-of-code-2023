from sys import stdin
from functools import cache
from collections import defaultdict
import heapq

class PrioQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = "<removed-task>"
        self.counter = 0

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
        
        entry = [priority, self.counter, task]
        self.counter += 1
        self.entry_finder[task] = entry
        heapq.heappush(self.heap, entry)
    
    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
    
    def pop_task(self):
        while self.heap:
            priority, _, task = heapq.heappop(self.heap)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError("pop from an empty priority queue")

    def __len__(self):
        return len(self.entry_finder)
    
    def __contains__(self, task):
        return task in self.entry_finder

@cache
def is_out_of_bounds(position, rows, columns):
    return position[0] < 0 or position[1] < 0 or position[0] >= rows or position[1] >= columns

def calculate_steps_without_turn(node, adjacent_direction_name):
    if node[2] == adjacent_direction_name:
        return node[3] + 1
    else:
        return 1

def neighbours(graph, node):
    neighbours = []

    for adjacent_direction, direction_name in [((0, 1), "E"), ((1, 0), "S"), ((0, -1), "W"), ((-1, 0), "N")]:
        new_position = (node[0] + adjacent_direction[0], node[1] + adjacent_direction[1])
        steps_without_turn = calculate_steps_without_turn(node, direction_name)

        if steps_without_turn > 10 or is_out_of_bounds(new_position, len(graph), len(graph[0])):
            continue

        if node[3] < 4 and node[2] is not None and node[2] != direction_name:
            continue
        
        neighbours.append((*new_position, direction_name, steps_without_turn))
    
    return neighbours


def cost(graph, position_1, position_2):
    return graph[position_2[0]][position_2[1]]

def cost_old(graph, position_1, position_2):
    if position_1[0] == position_2[0]:
        inicio, fin = sorted([position_1[1]+1, position_2[1]+1])
        return sum(graph[position_1[0]][inicio:fin])
    else:
        inicio, fin = sorted([position_1[0]+1, position_2[0]+1])
        return sum(graph[i][position_1[1]] for i in range(inicio, fin))


def dijkstra(graph, start_position, end_position):
    distance = defaultdict(lambda: float("inf"))
    global_minimum = float("inf")
    previous = {}

    start_node = (*start_position, None, 0)

    distance[start_node] = 0

    alive_nodes = PrioQueue()
    already_visited = set()

    for n in neighbours(graph, start_node):
        distance[n] = cost(graph, start_position, n)
        previous[n] = start_node
        alive_nodes.add_task(n, distance[n])

    while alive_nodes:
        u = alive_nodes.pop_task()
        already_visited.add(u)

        if u[:2] == end_position:
            # ???????????????????
            global_minimum = min(global_minimum, distance[u])
            continue

        for n in neighbours(graph, u):
            if previous[u][:2] == n[:2]:
                # don't go back
                continue

            if n not in already_visited and distance[n] > distance[u] + cost(graph, u, n):
                distance[n] = distance[u] + cost(graph, u, n)
                previous[n] = u
                if n in alive_nodes:
                    alive_nodes.remove_task(n)
                alive_nodes.add_task(n, distance[n])

    return distance, previous


cost_map = [[int(c) for c in l.strip()] for l in stdin.readlines()]

start_position = (0, 0)
end = (len(cost_map) - 1, len(cost_map[0]) - 1)

distance, previous = dijkstra(cost_map, start_position, end)

str_cost_map = [[str(c) for c in row] for row in cost_map]

min_end_node = min((k for k in distance if k[:2] == end and k[3] >= 4), key=lambda x: distance[x])
current_node = min_end_node


while current_node in previous:
    str_cost_map[current_node[0]][current_node[1]] = "X"
    current_node = previous[current_node]

print("\n".join("".join(row) for row in str_cost_map))

print(distance[min_end_node])