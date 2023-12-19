import re

def no_exception_input():
    try:
        return input()
    except EOFError:
        return None

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


parts = []
part = input()

while part:
    # strip first { and last }
    part = part[1:-1]

    variable_values = part.split(",")
    part_variables = {}
    
    for v in variable_values:
        variable, value = v.split("=")
        value = int(value)
        part_variables[variable] = value
    
    parts.append(part_variables)

    part = no_exception_input()

count = 0

for p in parts:
    workflow = workflows["in"]

    destination = get_destination(p, workflow)

    while destination not in "AR":
        workflow = workflows[destination]
        destination = get_destination(p, workflow)
    
    if destination == "A":
        count += sum(p.values())

print(count)
