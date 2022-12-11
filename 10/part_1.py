content = str(open("./10/inputs.txt", "r").read())

cycles = [1]

for instruction in content.split("\n"):
    if instruction == "noop":
        if len(cycles) == 0:
            cycles.append(1)
        else:
            cycles.append(cycles[-1])
    else:
        x = int(instruction.split(" ")[1])

        for _ in range(1):
            if len(cycles) == 0:
                cycles.append(1)
            else:
                cycles.append(cycles[-1])

        cycles.append(cycles[-1] + x)

score = sum([cycles[s-1] * s for s in [20, 60, 100, 140, 180, 220]])
print(score)
