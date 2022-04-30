c = int(input())
op = input()

m = []
  
for i in range(0, 12):
    m.append([])
    for j in range(0, 12):
        m[i].append(float(input()))

soma = 0

for i in range(0, 12):
    soma += m[i][c]

if op == "S":
    print(f"{soma:.1f}")
elif op == "M":
    print(f"{soma/12:.1f}")