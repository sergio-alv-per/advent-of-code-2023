def custom_hash(string):
    h = 0
    for c in string:
        h += ord(c)
        h *= 17
        h %= 256
    return h

line = input()
steps = line.split(',')

count = 0
for step in steps:
    count += custom_hash(step)

print(count)