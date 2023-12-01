from sys import stdin

total = 0

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in stdin:
    firstPosition = 10000000
    first = None
    lastPosition = -1
    last = None

    for i, c in enumerate(line):
        if c.isnumeric():
            if i < firstPosition:
                firstPosition = i
                first = c
            if i > lastPosition:
                lastPosition = i
                last = c
    
    for n in numbers:
        firstOccurrence = line.find(n)
        if firstOccurrence != -1:
            if firstOccurrence < firstPosition:
                firstPosition = firstOccurrence
                first = numbers[n]
            
            lastOccurrence = line.rfind(n)
            if lastOccurrence > lastPosition:
                lastPosition = lastOccurrence
                last = numbers[n]
    
    calibration = int(first + last)

    #print(calibration)
    
    total += calibration

print(total)
