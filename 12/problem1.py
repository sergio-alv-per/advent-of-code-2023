from sys import stdin
import re
from itertools import combinations

sum_of_counts = 0
for line in (l.rstrip() for l in stdin):
    damaged_spring_groups = [int(m) for m in re.findall(r"(\d+)", line)]
    springs = list(line[:line.find(" ")])
    unkowns = [i for i in range(len(springs)) if springs[i] == "?"]
    number_missing_springs = sum(damaged_spring_groups) - line.count("#")

    for comb in combinations(unkowns, number_missing_springs):
        springs_copy = springs[:]
        for i in comb:
            springs_copy[i] = "#"
        springs_setup = "".join(springs_copy).replace("?",".")
        
        all_match = True
        for i, match in enumerate(re.findall(r"#+", springs_setup)):
            if len(match) != damaged_spring_groups[i]:
                all_match = False
                break
        
        if all_match:
            sum_of_counts += 1

print(sum_of_counts)
        
    