n = int(input())
estrelas = [int(i) for i in input().split()]
total = sum(estrelas)
estrelasAtacadas = [0] * n
i = 0

while i >= 0 and i < n:
    direcao = estrelas[i] % 2
    if estrelas[i] > 0:
        estrelas[i] -= 1
        estrelasAtacadas[i] = 1
        total -= 1
    if direcao:
        i += 1
    else:
        i -= 1

estrelasAtacadas = estrelasAtacadas.count(1)
print(estrelasAtacadas, total)