list1 = []
list2 = []
total = 0;

with open('./01/input.txt') as f:
    for line in f:
        i1, i2 = line.split()
        list1 += [int(i1)]
        list2 += [int(i2)]

list1.sort()
list2.sort()

for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
output = open('./01/output1.txt', 'w')
output.write(str(total))
