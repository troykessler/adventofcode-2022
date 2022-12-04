content = str(open("./4/inputs.txt", "r").read())

p = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in content.split("\n")]
y = lambda e1, e2: e2[0] <= e1[0] <= e2[1] or e2[0] <= e1[1] <= e2[1]
s = sum([1 if y(g[0], g[1]) or y(g[1], g[0]) else 0 for g in p])
print(s)
