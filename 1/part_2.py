content = str(open("./1/inputs.txt", "r").read())

s = sorted([sum([int(y) for y in x.split("\n")]) for x in content.split("\n\n")])
print(sum(s[-3:]))
