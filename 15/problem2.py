def custom_hash(string):
    h = 0
    for c in string:
        h += ord(c)
        h *= 17
        h %= 256 
    return h

def assign_lens(label, focal_length, hashmap):
    for lens in hashmap[custom_hash(label)]:
        if lens[0] == label:
            lens[1] = focal_length
            return
    hashmap[custom_hash(label)].append([label, focal_length])

def calculate_focusing_power(hashmap):
    count = 0
    for i, box in enumerate(hashmap, start=1):
        for slot, lens in enumerate(box, start=1):
            count += i * slot * lens[1]
    
    return count

line = input()
steps = line.split(',')
hashmap = [[] for _ in range(256)]
for step in steps:
    if step[-1] == "-":
        # remove instruction
        label = step[:-1]
        hashmap[custom_hash(label)] = [lens for lens in hashmap[custom_hash(label)] if lens[0] != label]
    else:
        # assign instruction
        label, focal_length = step.split("=")
        focal_length = int(focal_length)
        assign_lens(label, focal_length, hashmap)
        
print(calculate_focusing_power(hashmap))