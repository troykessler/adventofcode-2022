signal = list(str(open("./6/inputs.txt", "r").read()))
n = 14

for i in range(len(signal)):
    if len(set(signal[i-n:i])) == n:
        print(i)
        break
