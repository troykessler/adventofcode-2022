content = str(open("./4/inputs.txt", "r").read())

p = [[[int(z) for z in y.split("-")] for y in x.split(",")] for x in content.split("\n")]
y = lambda x1, x2: x2[0] <= x1[0] <= x2[1] or x2[0] <= x1[1] <= x2[1]
s = sum([1 if y(x0, x1) or y(x1, x0) else 0 for [x0, x1] in p])
print(s)
