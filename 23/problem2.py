from sys import stdin
from collections import namedtuple, defaultdict

Point = namedtuple('Point', ["i", "j"])

def load_labyrinth():
    labyrinth = []

    for line in stdin:
        labyrinth.append(line.strip().replace(">", ".").replace("v", "."))

    labyrinth.insert(0, "#" * len(labyrinth[0]))
    labyrinth.append("#" * len(labyrinth[0]))

    return labyrinth

def generate_graph(labyrinth):
    graph = defaultdict(dict)
    reached = set()

    first = Point(1, 1)
    second = Point(2, 1)
    last = Point(len(labyrinth) - 2, len(labyrinth[-1]) - 2)

    open_queue = [(first, second)]

    while open_queue:
        path = open_queue.pop(0)
        origin = path[0]
        previous = path[-2]
        current = path[-1]

        adjacents = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_point = Point(current.i+di, current.j+dj)
            if next_point != previous and labyrinth[next_point.i][next_point.j] == ".":
                adjacents.append(next_point)
        
        if len(adjacents) == 0:
            # current is last
            graph[origin][current] = len(path) - 1
        elif len(adjacents) > 1:
            # current is an intersection
            if current not in graph[origin]:
                graph[origin][current] = len(path) - 1
            else:
                graph[origin][current] = max(graph[origin][current], len(path) - 1)

            if current not in reached:
                for adjacent in adjacents:
                    open_queue.append((current, adjacent))
        else:
            # current is normal path
            open_queue.append(path + tuple(adjacents))
        
        reached.add(current)

    # Symetrize
    base_keys = list(graph.keys())
    for origin in base_keys:
        for destination in graph[origin]:
            graph[destination][origin] = graph[origin][destination]
    
    # Remove paths going from last
    graph[last] = {}

    return graph

def visualize_intersections(labyrinth, graph):
    labyrinth_vis = [[c if c != "." else " " for c in row] for row in labyrinth]

    for i, origin in enumerate(graph):
        labyrinth_vis[origin.i][origin.j] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]

    print("\n".join("".join(row) for row in labyrinth_vis))

def visualize_graph(graph, last):
    vis_dict = {}
    for i, origin in enumerate(graph):
        vis_dict[origin] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]

    for origin in graph:
        for destination in graph[origin]:
            if vis_dict[origin] < vis_dict[destination]or destination == last:
                print(f"{vis_dict[origin]} -> {vis_dict[destination]}: {graph[origin][destination]}")

def length(path, graph):
    return sum(graph[origin][destination] for origin, destination in zip(path[:-1], path[1:]))

def longest_path(graph, first, last):
    # Running this takes way too long but DFS finds the longest path (6542)
    # quickly. The rest is evaluating paths that end up being shorter.
    longest_path = None
    longest_distance = 0
    open_stack = [(first,)]

    while open_stack:
        path = open_stack.pop()
        current = path[-1]

        if current == last:
            if length(path, graph) > longest_distance:
                longest_distance = length(path, graph)
                longest_path = path
                print(f"New longest path distance: {longest_distance}")
                continue

        for adjacent in graph[current]:
            if adjacent not in path:
                open_stack.append(path + (adjacent,))
    
    return longest_path, longest_distance

labyrinth = load_labyrinth()
graph = generate_graph(labyrinth)
start = Point(1, 1)
end = Point(len(labyrinth) - 2, len(labyrinth[-1]) - 2)
_, longest_distance = longest_path(graph, start, end)
print(longest_distance)






