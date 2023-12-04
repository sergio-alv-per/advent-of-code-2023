from sys import stdin
import re

suma = 0
for line in map(str.strip, stdin):

    line = line.split(": ")[1]
    winning, have = line.split(" | ")

    winning = set(re.findall(r"\d+", winning))
    have = set(re.findall(r"\d+", have))

    if len(winning & have) > 0:
        suma += 2**(len(winning & have)-1)

print(suma)
