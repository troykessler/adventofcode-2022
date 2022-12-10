content = str(open("./9/inputs.txt", "r").read())

head = [0, 0]  # x, y
tail = [0, 0]  # x, y
path = [str(tail)]

for c in content.split("\n"):
    direction = c.split(" ")[0]
    steps = int(c.split(" ")[1])

    if direction == "U":
        for _ in range(steps):
            head[1] += 1

            if abs(head[1] - tail[1]) > 1:
                tail[0] = head[0]
                tail[1] += 1
                path.append(str(tail))

    if direction == "R":
        for _ in range(steps):
            head[0] += 1

            if abs(head[0] - tail[0]) > 1:
                tail[0] += 1
                tail[1] = head[1]
                path.append(str(tail))

    if direction == "D":
        for _ in range(steps):
            head[1] -= 1

            if abs(head[1] - tail[1]) > 1:
                tail[0] = head[0]
                tail[1] -= 1
                path.append(str(tail))

    if direction == "L":
        for _ in range(steps):
            head[0] -= 1

            if abs(head[0] - tail[0]) > 1:
                tail[0] -= 1
                tail[1] = head[1]
                path.append(str(tail))

print(len(set(path)))
