content = str(open("./8/inputs.txt", "r").read())

trees = [[int(t) for t in list(row)] for row in content.split("\n")]


def count_left(x, y):
    count = 0
    y1 = y - 1

    while y1 >= 0:
        count += 1

        if trees[x][y1] >= trees[x][y]:
            break

        y1 -= 1

    return count


def count_right(x, y):
    count = 0
    y1 = y + 1

    while y1 <= len(trees[x])-1:
        count += 1

        if trees[x][y1] >= trees[x][y]:
            break

        y1 += 1

    return count


def count_top(x, y):
    count = 0
    x1 = x - 1

    while x1 >= 0:
        count += 1

        if trees[x1][y] >= trees[x][y]:
            break

        x1 -= 1

    return count


def count_bottom(x, y):
    count = 0
    x1 = x + 1

    while x1 <= len(trees)-1:
        count += 1

        if trees[x1][y] >= trees[x][y]:
            break

        x1 += 1

    return count


score = 0

for x in range(len(trees)):
    for y in range(len(trees[x])):
        tree = count_left(x, y) * count_right(x, y) * count_top(x, y) * count_bottom(x, y)

        if tree > score:
            score = tree

print(score)
