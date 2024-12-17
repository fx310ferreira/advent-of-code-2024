total = 0
with open("./02/input.txt") as f:
    for line in f:
        values = list(map(int, line.split()))
        last = values[0]
        step = 0
        valid = True
        for i in values[1:]:
            new_step = i - last
            last = i
            if abs(new_step) < 1 or abs(new_step) > 3 or new_step * step < 0:
                valid = False
                break
            step = new_step
        if valid:
            total += 1
output = open("./02/output1.txt", "w") 
output.write(str(total))