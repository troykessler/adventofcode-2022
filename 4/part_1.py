content = str(open("./4/inputs.txt", "r").read())

p = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in content.split("\n")]
s = sum([1 if (x0[0] >= x1[0] and x0[1] <= x1[1]) or (x1[0] >= x0[0] and x1[1] <= x0[1]) else 0 for [x0, x1] in p])
print(s)
