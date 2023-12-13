from sys import stdin
import re

def check_horizontal_reflections(ash_map):
    for reflection_axis in range(1, len(ash_map)):
        distance_to_borders = min(reflection_axis, len(ash_map) - reflection_axis)

        reflection_exists = True
        for offset in range(distance_to_borders):
            line = ash_map[reflection_axis - 1 - offset]
            reflection = ash_map[reflection_axis + offset]

            if line != reflection:
                reflection_exists = False
                break
        
        if reflection_exists:
            return reflection_axis
    
    return 0

full_text = "".join(stdin.readlines())
maps = [m.group(0) for m in re.finditer(r"([.#]+\n)+", full_text, re.MULTILINE)]
maps = [[list(line) for line in m.split("\n")[:-1]] for m in maps]

count = 0
for ash_map in maps:
    map_transposed = [list(col) for col in zip(*ash_map)]
    
    count += 100 * check_horizontal_reflections(ash_map)
    count += check_horizontal_reflections(map_transposed)

print(count)




