n = int(input())

anterior = 0
atual = 1
proximo = 0

sequencia = []

for i in range(n):
    sequencia.append(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo

for i in range(n-1, -1, -1):
    if i == 0:
        print(f"{sequencia[i]}")
    else:
        print(f"{sequencia[i]}", end = " ")