from sys import stdin
from math import lcm

class Module:
    def __init__(self, type, state, destinations):
        self.type = type
        self.state = state
        self.destinations = destinations
    
    def __str__(self):
        return f"Module(type={self.type}, state={self.state}, destinations={self.destinations}))"
    
    def __repr__(self):
        return str(self)

def flip(state):
    if state == "L":
        return "H"
    else:
        return "L"

def get_conjunction_modules_and_inputs(module_graph):
    initial_modules = module_graph["broadcaster"].destinations

    conjunction_modules_inputs = {}

    for im in initial_modules:
        chain = [im]
        conj, next_in_chain = module_graph[im].destinations

        if module_graph[conj].type == "%":
            conj, next_in_chain = next_in_chain, conj
        
        while next_in_chain:
            chain.append(next_in_chain)
            
            next_in_chain_set = set(module_graph[next_in_chain].destinations)
            next_in_chain_set.discard(conj)

            if next_in_chain_set:
                next_in_chain = next_in_chain_set.pop()
            else:
                next_in_chain = None

        conjunction_modules_inputs[conj] = tuple(chain)
    
    return conjunction_modules_inputs

def print_states(module, inputs, module_graph):
    print(f"{module} - " + " ".join(("\033[92m" if module_graph[m].state == "H" else "\033[91m") + m for m in inputs) + "\033[0m")
    
module_graph = {}

for line in (l.strip() for l in stdin):
    module_name, destination_modules = line.split(" -> ")
    destination_modules = destination_modules.split(", ")

    if module_name == "broadcaster":
        module_graph[module_name] = Module("B", None, destination_modules)
    else:
        module_type = module_name[0]
        module_name = module_name[1:]
        module_graph[module_name] = Module(module_type, None, destination_modules)

        if module_type == "%":
            module_graph[module_name].state = "L"
        elif module_type == "&":
            module_graph[module_name].state = {}

for module_name, module in module_graph.items():
    for d in module.destinations:
        if d in module_graph and module_graph[d].type == "&":
            module_graph[d].state[module_name] = "L"

conjunction_modules = get_conjunction_modules_and_inputs(module_graph)

pulses = {"L": 0, "H": 0}
cycle_for_module = {m: 0 for m in conjunction_modules}
button_presses = 0
while not all(cycle_for_module.values()):
    button_presses += 1
    pulse_queue = [("button", "broadcaster", "L")]
    pulses["L"] += 1
    while pulse_queue:            
        origin_module, module_name, pulse_type = pulse_queue.pop(0)
        
        if module_name not in module_graph:
            continue

        module = module_graph[module_name]

        sent_pulse_type = None

        if module.type == "B":
            sent_pulse_type = pulse_type
        elif module.type == "%":
            if pulse_type == "L":
                module.state = flip(module.state)
                sent_pulse_type = module.state
            else:
                continue
        elif module.type == "&":
            module.state[origin_module] = pulse_type
            if all(s == "H" for s in module.state.values()):
                sent_pulse_type = "L"
                if module_name in conjunction_modules:
                    print(f"Module {module_name} activated at button press {button_presses}")
                    print_states(module_name, conjunction_modules[module_name], module_graph)
                    cycle_for_module[module_name] = button_presses
            else:
                sent_pulse_type = "H"
        
        pulse_queue.extend((module_name, next_module, sent_pulse_type) for next_module in module.destinations)
        pulses[sent_pulse_type] += len(module.destinations)
    

print(f"Least common multiple of cycles for modules: {lcm(*cycle_for_module.values())}")

