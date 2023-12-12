from sys import stdin
import re
from functools import cache

@cache
def possibilities(springs, damaged_springs_groups):
    count = 0
    if not damaged_springs_groups:
        # No more damaged springs to place
        if "#" in springs:
            # Damaged spring in path, not valid
            return 0
        else:
            # No damaged springs in path. Path would be only one way,
            # substituting all "?" with ".".
            return 1
    else:
        current_group_size = damaged_springs_groups[0]
        if len(springs) < current_group_size:
            # Not enough space to fit the damaged springs
            return 0
        else:
            if "." not in springs[:current_group_size]:
                # Spring map starts only with "#" or "?", could be valid
                if (len(springs) == current_group_size # End of spring map
                    or springs[current_group_size] != "#"): # Will be able to end the spring group
                    # Place the spring group AND A "." at the start of the string, and then get the remaining possibilities
                    count += possibilities(springs[current_group_size+1:], damaged_springs_groups[1:])
            
            # After trying to place the spring group at the start, try to place
            # a "." at the start and then get the possibilities
            if springs[0] != "#":
                # Place a "." at the start, and then get the remaining possibilities
                count += possibilities(springs[1:], damaged_springs_groups)
    
    return count

sum_of_counts = 0
for line in (l.rstrip() for l in stdin):
    damaged_springs_groups = [int(m) for m in re.findall(r"(\d+)", line)] * 5
    springs = line[:line.find(" ")]
    springs = "?".join([springs]*5)
    springs = re.sub(r"\.{2,}", ".", springs)
    springs = springs.strip(".")

    count = possibilities(springs, tuple(damaged_springs_groups))

    sum_of_counts += count

print(sum_of_counts)
    