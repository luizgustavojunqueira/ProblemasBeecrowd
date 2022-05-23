n = int(input())

pomekonsDiferentes = []

for i in range(n):
    p = input()
    if p not in pomekonsDiferentes:
        pomekonsDiferentes.append(p)

print(f"Falta(m) {151-len(pomekonsDiferentes)} pomekon(s).")