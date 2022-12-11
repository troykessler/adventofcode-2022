content = str(open("./10/inputs.txt", "r").read())

cycles = [1]

for instruction in content.split("\n"):
    cycles.append(cycles[-1])

    if instruction != "noop":
        cycles.append(cycles[-1] + int(instruction.split(" ")[1]))

for row in range(6):
    pixels = ""

    for position in range(40):
        cycle = row * 40 + position
        sprite = cycles[cycle]

        if position in [sprite - 1, sprite, sprite + 1]:
            pixels += "#"
        else:
            pixels += "."

    print(pixels)
