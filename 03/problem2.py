import re

total = 0
add = True
with open('./03/input.txt') as f:
    for line in f:
        matches = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
        for match in matches:
            if (match == "do()"):
                add = True
            elif (match == "don't()"):
                add = False
            elif add:
                values = match[4:-1].split(',')
                total += int(values[0]) * int(values[1])

open('./03/output2.txt', 'w').write(str(total))