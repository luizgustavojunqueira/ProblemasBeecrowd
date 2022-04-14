op = input()

m = []

for i in range(0, 12):
    m.append([])
    for j in range(0, 12):
        m[i].append(float(input()))

soma = 0
numElementos = 0

for i in range(0, 12):
    for k in range(0, i):
        soma += m[i][k]
        numElementos += 1

if op == "S":
    print(f"{soma:.1f}")
elif op == "M":
    print(f"{soma/numElementos:.1f}")