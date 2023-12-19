import re
from math import prod


def get_destination(part, workflow):
    for rule in workflow:
        variable, comparator, value, destination = rule
        if variable == "E":
            return destination
        else:
            if comparator == ">":
                if part[variable] > value:
                    return destination
            else:
                if part[variable] < value:
                    return destination

def evaluate_range_on_workflow(values_range, workflow):
    ranges_with_destinations = []
    working_range = values_range.copy()
    for rule in workflow:
        variable, comparator, value, destination = rule
        if variable == "E":
            ranges_with_destinations.append((working_range, destination))
            return ranges_with_destinations
        else:
            var_lower_bound = working_range[variable][0]
            var_upper_bound = working_range[variable][1]
            if comparator == ">":
                if value < var_lower_bound:
                    ranges_with_destinations.append((working_range, destination))
                    return ranges_with_destinations
                elif var_lower_bound <= value < var_upper_bound:
                    new_range = working_range.copy()
                    new_range[variable] = (value + 1, var_upper_bound)
                    ranges_with_destinations.append((new_range, destination))
                    working_range[variable] = (var_lower_bound, value)
                else:
                    continue
            else:
                if value > var_upper_bound:
                    ranges_with_destinations.append((working_range, destination))
                    return ranges_with_destinations
                elif var_lower_bound < value <= var_upper_bound:
                    new_range = working_range.copy()
                    new_range[variable] = (var_lower_bound, value - 1)
                    ranges_with_destinations.append((new_range, destination))
                    working_range[variable] = (value, var_upper_bound)
                else:
                    continue
    
    return ranges_with_destinations


workflows = {}

workflow = input()

while workflow:
    name, rules = re.match(r"([a-z]+){(.*)}", workflow).groups()
    rules = rules.split(",")
    processed_rules = []
    for r in rules:
        if ":" in r:
            rule, destination = r.split(":")
            variable = rule[0]
            comparator = rule[1]
            value = int(rule[2:])
            processed_rules.append((variable, comparator, value, destination))
        else:
            processed_rules.append(("E", None, None, r))
    
    workflows[name] = processed_rules
    workflow = input()

total_combinations = 4000*4000*4000*4000

values_range = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
initial_destination = "in"

queue = [(values_range, initial_destination)]

while queue:
    values_range, destination = queue.pop(0)
    
    if destination == "A":
        continue
    elif destination == "R":
        total_combinations -= prod(r[1] - r[0] + 1 for r in values_range.values())
    else:
        workflow = workflows[destination]
        queue.extend(evaluate_range_on_workflow(values_range, workflow))

print(total_combinations)
