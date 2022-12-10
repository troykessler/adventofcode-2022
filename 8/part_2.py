content = str(open("./8/inputs.txt", "r").read())

trees = [[int(t) for t in list(row)] for row in content.split("\n")]


def calc_view(view):
    if len(view) == 0:
        return 0

    for i in range(1, len(view)):
        if view[i] >= view[0]:
            return i

    return len(view) - 1


score = 0

for x in range(len(trees)):
    for y in range(len(trees[x])):
        left = calc_view(trees[x][:y+1][::-1])
        right = calc_view(trees[x][y:])
        top = calc_view([row[y] for row in trees][:x+1][::-1])
        bottom = calc_view([row[y] for row in trees][x:])

        total = left * right * top * bottom

        if total > score:
            score = total

print(score)
