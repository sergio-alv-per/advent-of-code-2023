from sys import stdin

total = 0

for line in stdin:

    first = None
    last = None

    for c in line:
        if c.isnumeric():
            if first is None:
                first = c
                last = c
            else:
                last = c
    
    total += int(first + last)

print(total)
