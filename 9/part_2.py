content = str(open("./9/inputs.txt", "r").read())

rope = [[0, 0] for _ in range(10)]
path = [str(rope[-1])]


def print_debug(rope):
    test = []

    for y in range(-10, 10):
        t = []
        for x in range(-13, 13):
            if x == 0 and y == 0:
                t.append("s")
            elif [x, y] in rope:
                t.append(str(rope.index([x, y])))
            else:
                t.append(".")

        test.append("".join(t))

    for t in test[::-1]:
        print(t)


for c in content.split("\n"):
    direction = c.split(" ")[0]
    steps = int(c.split(" ")[1])

    if direction == "U":
        for _ in range(steps):
            rope[0][1] += 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][0] - rope[knot][0]) > 1 or abs(rope[knot-1][1] - rope[knot][1]) > 1:
                    if rope[knot-1][1] > rope[knot][1]:
                        rope[knot][1] += 1

                    if rope[knot-1][1] < rope[knot][1]:
                        rope[knot][1] -= 1

                    if rope[knot-1][0] > rope[knot][0]:
                        rope[knot][0] += 1

                    if rope[knot-1][0] < rope[knot][0]:
                        rope[knot][0] -= 1

            path.append(str(rope[-1]))

    if direction == "R":
        for _ in range(steps):
            rope[0][0] += 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][0] - rope[knot][0]) > 1 or abs(rope[knot-1][1] - rope[knot][1]) > 1:
                    if rope[knot - 1][1] > rope[knot][1]:
                        rope[knot][1] += 1

                    if rope[knot - 1][1] < rope[knot][1]:
                        rope[knot][1] -= 1

                    if rope[knot - 1][0] > rope[knot][0]:
                        rope[knot][0] += 1

                    if rope[knot - 1][0] < rope[knot][0]:
                        rope[knot][0] -= 1

            path.append(str(rope[-1]))

    if direction == "D":
        for _ in range(steps):
            rope[0][1] -= 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][0] - rope[knot][0]) > 1 or abs(rope[knot-1][1] - rope[knot][1]) > 1:
                    if rope[knot - 1][1] > rope[knot][1]:
                        rope[knot][1] += 1

                    if rope[knot - 1][1] < rope[knot][1]:
                        rope[knot][1] -= 1

                    if rope[knot - 1][0] > rope[knot][0]:
                        rope[knot][0] += 1

                    if rope[knot - 1][0] < rope[knot][0]:
                        rope[knot][0] -= 1

            path.append(str(rope[-1]))

    if direction == "L":
        for _ in range(steps):
            rope[0][0] -= 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][0] - rope[knot][0]) > 1 or abs(rope[knot-1][1] - rope[knot][1]) > 1:
                    if rope[knot - 1][1] > rope[knot][1]:
                        rope[knot][1] += 1

                    if rope[knot - 1][1] < rope[knot][1]:
                        rope[knot][1] -= 1

                    if rope[knot - 1][0] > rope[knot][0]:
                        rope[knot][0] += 1

                    if rope[knot - 1][0] < rope[knot][0]:
                        rope[knot][0] -= 1

            path.append(str(rope[-1]))

print(len(set(path)))
