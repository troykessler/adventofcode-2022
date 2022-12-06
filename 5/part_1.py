content = str(open("./5/inputs.txt", "r").read())

instructions = content.split("\n")[10:]
supplies = [
    ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
    ['T', 'B', 'M', 'Z', 'R'],
    ['Z', 'L', 'C', 'H', 'N', 'S'],
    ['S', 'C', 'F', 'J'],
    ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    ['M', 'Z', 'R'],
    ['M', 'C', 'L', 'G', 'V', 'R', 'T']
]

for raw in instructions:
    instruction = raw.split(" ")

    crates = int(instruction[1])
    fromStack = int(instruction[3]) - 1
    toStack = int(instruction[5]) - 1

    for _ in range(crates):
        item = supplies[fromStack].pop()
        supplies[toStack].append(item)

print("".join([stack[-1] for stack in supplies]))
