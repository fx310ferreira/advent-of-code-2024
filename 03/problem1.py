import re

total = 0
with open('./03/input.txt') as f:
    for line in f:
        matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
        for match in matches:
            values = match[4:-1].split(',')
            total += int(values[0]) * int(values[1])

open('./03/output1.txt', 'w').write(str(total))