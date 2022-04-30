n = int(input())

valores = input().split()

multi2 = 0
multi3 = 0
multi4 = 0
multi5 = 0

for i in range(n):
    valores[i] = int(valores[i])
    if valores[i] % 2 == 0:
        multi2 += 1
    if valores[i] % 3 == 0:
        multi3 += 1
    if valores[i] % 4 == 0:
        multi4 += 1
    if valores[i] % 5 == 0:
        multi5 += 1

print(f"{multi2} Multiplo(s) de 2")
print(f"{multi3} Multiplo(s) de 3")
print(f"{multi4} Multiplo(s) de 4")
print(f"{multi5} Multiplo(s) de 5")