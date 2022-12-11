content = str(open("./9/inputs.txt", "r").read())

rope = [[0, 0] for _ in range(10)]
path = [str(rope[-1])]

for c in content.split("\n"):
    direction = c.split(" ")[0]
    steps = int(c.split(" ")[1])

    if direction == "U":
        for _ in range(steps):
            rope[0][1] += 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][1] - rope[knot][1]) > 1:
                    rope[knot][0] = rope[knot-1][0]
                    rope[knot][1] += 1

            path.append(str(rope[-1]))
            print(direction, rope)

    if direction == "R":
        for _ in range(steps):
            rope[0][0] += 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][0] - rope[knot][0]) > 1:
                    rope[knot][0] += 1
                    rope[knot][1] = rope[knot-1][1]

            path.append(str(rope[-1]))
            print(direction, rope)

    if direction == "D":
        for _ in range(steps):
            rope[0][1] -= 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][1] - rope[knot][1]) > 1:
                    rope[knot][0] = rope[knot-1][0]
                    rope[knot][1] -= 1

            path.append(str(rope[-1]))
            print(direction, rope)

    if direction == "L":
        for _ in range(steps):
            rope[0][0] -= 1

            for knot in range(1, len(rope)):
                if abs(rope[knot-1][0] - rope[knot][0]) > 1:
                    rope[knot][0] -= 1
                    rope[knot][1] = rope[knot-1][1]

            path.append(str(rope[-1]))
            print(direction, rope)

print(len(set(path)))
