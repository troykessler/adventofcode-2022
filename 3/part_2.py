content = str(open("./3/inputs.txt", "r").read())

p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = [content.split("\n")[i:i+3] for i in range(0, len(content.split("\n")), 3)]
s = sum([p.index(set(y[0]).intersection(set(y[1]), set(y[2])).pop()) + 1 for y in x])
print(s)
