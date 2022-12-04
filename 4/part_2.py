f = open("./4/inputs.txt", "r")
content = f.read().split("\n")

score = 0

for c in content:
    pairs = list(map(lambda p: list(map(lambda i: int(i), p.split("-"))), c.split(",")))

    if pairs[1][0] <= pairs[0][0] <= pairs[1][1] or pairs[1][0] <= pairs[0][1] <= pairs[1][1]:
        score += 1
        continue

    if pairs[0][0] <= pairs[1][0] <= pairs[0][1] or pairs[0][0] <= pairs[1][1] <= pairs[0][1]:
        score += 1
        continue

print(score)
