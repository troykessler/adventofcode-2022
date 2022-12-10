content = str(open("./8/inputs.txt", "r").read())

trees = [[int(t) for t in list(row)] for row in content.split("\n")]

visible = 0

for x in range(len(trees)):
    for y in range(len(trees[x])):
        tree = trees[x][y]

        # edge
        if x == 0 or y == 0 or x == len(trees)-1 or y == len(trees[x])-1:
            visible += 1
            continue

        # left
        if max(trees[x][:y]) < tree:
            visible += 1
            continue

        # right
        if max(trees[x][y+1:]) < tree:
            visible += 1
            continue

        # top
        if max([row[y] for row in trees][:x]) < tree:
            visible += 1
            continue

        # bottom
        if max([row[y] for row in trees][x+1:]) < tree:
            visible += 1
            continue

print(visible)
