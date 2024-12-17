list1 = []
list2 = {}
total = 0;

with open('./01/input.txt') as f:
    for line in f:
        i1, i2 = line.split()
        list1 += [int(i1)]
        if (int(i2) in list2):
            list2[int(i2)] += 1
        else:
            list2[int(i2)] = 1

list1.sort()
total = 0;

for i in list1:
    if (i in list2):
        total += (i*list2[i])
    else:
        total += 0

output = open('./01/output2.txt', 'w')
output.write(str(total))
