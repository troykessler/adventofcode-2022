content = str(open("./4/inputs.txt", "r").read())

p = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in content.split("\n")]
s = [1 if (g[0][0] >= g[1][0] and g[0][1] <= g[1][1]) or (g[1][0] >= g[0][0] and g[1][1] <= g[0][1]) else 0 for g in p]
print(sum(s))
