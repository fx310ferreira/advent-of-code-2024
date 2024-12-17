total = 0
with open("./02/input.txt") as f:
    for line in f:
        values = list(map(int, line.split()))
        last = values[0]
        step = 0
        invalid = 0
        invalid_reverse = 0
        for i in range(1, len(values)):
            new_step = values[i] - last
            if abs(new_step) < 1 or abs(new_step) > 3 or new_step * step < 0:
                invalid += 1
            else:
                last = values[i]
                step = new_step

        last = values[-1]
        step = 0
        invalid_reverse = 0
        for i in range(len(values) -2, -1, -1):
            new_step = values[i] - last
            if abs(new_step) < 1 or abs(new_step) > 3 or new_step * step < 0:
                invalid_reverse += 1
            else:
                last = values[i]
                step = new_step
        if invalid < 2 or invalid_reverse < 2:
            total += 1

output = open("./02/output2.txt", "w") 
output.write(str(total))