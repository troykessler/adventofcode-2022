content = str(open("./10/inputs.txt", "r").read())

cycles = [1]

for instruction in content.split("\n"):
    cycles.append(cycles[-1])

    if instruction != "noop":
        cycles.append(cycles[-1] + int(instruction.split(" ")[1]))

signal = sum([cycles[s-1] * s for s in [20, 60, 100, 140, 180, 220]])
print(signal)
