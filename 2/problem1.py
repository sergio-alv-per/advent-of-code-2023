from sys import stdin

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

id_sum = 0

for id, line in enumerate(stdin, start=1):
    line = line.strip()
    line = line[line.find(":")+2:]
    subsets = line.split("; ")

    possible = True

    for subset in subsets:
        subset = subset.split(", ")
        for s in subset:
            num, color = s.split(" ")
            num = int(num)

            if num > maxes[color]:
                possible = False
    
    if possible:
        id_sum += id

print(id_sum)

