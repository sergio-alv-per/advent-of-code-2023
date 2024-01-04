from sys import stdin

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



pulses = {"L": 0, "H": 0}
for button_presses in range(1, 1001):
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
            else:
                sent_pulse_type = "H"
        
        pulse_queue.extend((module_name, next_module, sent_pulse_type) for next_module in module.destinations)
        pulses[sent_pulse_type] += len(module.destinations)

print(pulses)
print(pulses["H"] * pulses["L"])
