from sys import stdin
import re
from collections import defaultdict

scratchcards = defaultdict(int)

for i, line in enumerate(map(str.strip, stdin)):
    scratchcards[i] += 1
    line = line.split(": ")[1]
    winning, have = line.split(" | ")

    winning = set(re.findall(r"\d+", winning))
    have = set(re.findall(r"\d+", have))

    for j in range(i+1, i+1+len(winning & have)):
        scratchcards[j] += scratchcards[i]

last_scratchcard = i

suma = 0
for k in range(last_scratchcard+1):
    suma += scratchcards[k]

print(suma)
