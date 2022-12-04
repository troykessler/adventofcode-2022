content = str(open("./1/inputs.txt", "r").read())

s = sum(sorted([sum([int(y) for y in x.split("\n")]) for x in content.split("\n\n")])[-3:])
print(s)
