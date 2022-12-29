content = str(open("./11/inputs.txt", "r").read())

monkeys = []

for m in content.split("\n\n"):
    monkey = {
        'inspections': 0
    }

    # read starting items
    monkey['items'] = list(map(lambda s: int(s), m.split("\n")[1].split(": ")[1].split(", ")))

    # read operation
    monkey['operation'] = eval('lambda old: ' + m.split("\n")[2].split(" = ")[1])

    # read test condition
    monkey['test'] = eval('lambda t: t % ' + m.split("\n")[3].split(" divisible by ")[1] + ' == 0')

    # read test divisor
    monkey['divisor'] = int(m.split("\n")[3].split(" divisible by ")[1])

    # read test success target
    monkey['True'] = int(m.split("\n")[4].split(" throw to monkey ")[1])

    # read test fail target
    monkey['False'] = int(m.split("\n")[5].split(" throw to monkey ")[1])

    monkeys.append(monkey)


for r in range(21):
    for m in range(len(monkeys)):
        for item in monkeys[m]['items']:
            # increase inspections
            monkeys[m]['inspections'] += 1

            worry = monkeys[m]['operation'](item) % monkeys[m]['divisor']
            target = monkeys[m][str(monkeys[m]['test'](worry))]

            monkeys[target]['items'].append(worry)

        monkeys[m]['items'] = []

# print(monkeys)
inspections = sorted(list(map(lambda monkey: monkey['inspections'], monkeys)))[-2:]
print(list(map(lambda monkey: monkey['items'], monkeys)))
print(list(map(lambda monkey: monkey['inspections'], monkeys)))
print(inspections[0] * inspections[1])
