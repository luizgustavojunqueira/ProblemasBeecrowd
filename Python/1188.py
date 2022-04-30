op = input()

m = []

soma = 0
nElementos = 0

for i in range(12):
    m.append([])
    for j in range(12):
        m[i].append(float(input()))
        if j > 11 -i and j<i:
            nElementos += 1
            soma += m[i][j]

if op == "S":
    print(f"{soma:.1f}")
elif op == "M":
    print(f"{soma/nElementos:.1f}")
    