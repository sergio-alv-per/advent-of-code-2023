from sys import stdin

power_sum = 0

for id, line in enumerate(stdin, start=1):
    line = line.strip()
    line = line[line.find(":")+2:]
    subsets = line.split("; ")

    minimums = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for subset in subsets:
        subset = subset.split(", ")
        for s in subset:
            num, color = s.split(" ")
            num = int(num)

            minimums[color] = max(minimums[color], num)
    
    power_sum += minimums["red"] * minimums["green"] * minimums["blue"]
    
print(power_sum)

