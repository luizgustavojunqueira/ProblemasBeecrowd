n = int(input())

qntVitorias = 0

for i in range(n):
    habilidadesUsadas = input()

    if "CD" not in habilidadesUsadas:
        qntVitorias += 1

print(qntVitorias)