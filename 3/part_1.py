content = str(open("./3/inputs.txt", "r").read())

p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = sum([p.index(set(r[:len(r) // 2]).intersection(set(r[len(r) // 2:])).pop()) + 1 for r in content.split("\n")])
print(s)
