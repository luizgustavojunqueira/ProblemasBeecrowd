valPositivos = 0
soma = 0

for i in range(0, 6):
    x = float(input())
    if x >= 0:
        valPositivos += 1
        soma += x

print(f"{valPositivos} valores positivos")
print(f"{(soma/valPositivos):.1f}")