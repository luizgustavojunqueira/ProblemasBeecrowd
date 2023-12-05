n = int(input())

nCarrinhos = 0
nBonecas = 0

for i in range(n):
    nome, sexo = input().split()

    if sexo == "M":
        nCarrinhos += 1
    else:
        nBonecas += 1

print(f"{nCarrinhos} carrinhos")
print(f"{nBonecas} bonecas")