content = str(open("./7/inputs.txt", "r").read())

pwd = []
state = {}

for c in content.split("\n"):
    if c.startswith("$ cd"):
        dirName = c.split(" ")[2]

        if dirName == "/":
            state["/"] = []
        elif dirName == "..":
            pwd.pop()
        else:
            pwd.append(dirName)

    elif c.startswith("dir "):
        dirName = c.split(" ")[1]
        path = "/" + "/".join(pwd)
        dirPath = path + "/" + dirName if len(pwd) > 0 else "/" + dirName

        state[path].append(dirPath)
        state[dirPath] = []
    elif not c.startswith("$ ls"):
        path = "/" + "/".join(pwd)
        state[path].append(int(c.split(" ")[0]))

size = 0


def get_dir_size(dir_path):
    s = 0

    for e in state[dir_path]:
        if type(e) == int:
            s += e
        else:
            s += get_dir_size(e)

    return s


for dirPath in state.keys():
    dirSize = get_dir_size(dirPath)

    if dirSize <= 100000:
        size += dirSize

print(size)
