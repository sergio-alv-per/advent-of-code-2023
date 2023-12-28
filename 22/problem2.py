from sys import stdin

blocks = []

max_x = max_y = 0

for line in (l.strip() for l in stdin):
    beginning, end = line.split("~")
    beginning = tuple(int(x) for x in beginning.split(","))
    end = tuple(int(x) for x in end.split(","))

    max_x = max(max_x, beginning[0], end[0])
    max_y = max(max_y, beginning[1], end[1])

    blocks.append((beginning, end))

# Sort in falling order
blocks = sorted(blocks, key=lambda x: x[0][2])

grid_height = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
grid_block = [[None for _ in range(max_x + 1)] for _ in range(max_y + 1)]

parent_graph = [set() for _ in range(len(blocks))]
in_degree = [0] * len(blocks)
base_blocks = set()

for i, block in enumerate(blocks):
    beginning, end = block
    max_height = 0
    for x in range(beginning[0], end[0] + 1):
        for y in range(beginning[1], end[1] + 1):
            max_height = max(max_height, grid_height[y][x])

    for x in range(beginning[0], end[0] + 1):
        for y in range(beginning[1], end[1] + 1):
            if grid_height[y][x]  == max_height:
                parent = grid_block[y][x]

                if parent is not None and i not in parent_graph[parent]:
                    parent_graph[parent].add(i)
                    in_degree[i] += 1
                elif parent is None:
                    base_blocks.add(i)

            grid_height[y][x] = max_height + (end[2] - beginning[2] + 1)
            grid_block[y][x] = i


sum_blocks_fallen = 0
for i in range(len(blocks)):
    traversal_queue = base_blocks.copy()
    traversal_queue.discard(i)
    traversed_blocks = set()
    n_traversed_blocks = 0

    while traversal_queue:
        block = traversal_queue.pop()
        if block in traversed_blocks:
            continue
        
        traversed_blocks.add(block)
        n_traversed_blocks += 1

        traversal_queue |= parent_graph[block]
        traversal_queue.discard(i)
    
    pass
    
    sum_blocks_fallen += len(blocks) - n_traversed_blocks - 1
            
print(sum_blocks_fallen)