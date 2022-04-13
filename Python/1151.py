n = int(input())

anterior = 0
atual = 0
proximo = 1

for i in range(0, n):
    if i == n-1:
        print(atual)
    else:
        print(atual, end=" ")
    anterior = atual
    atual = proximo
    proximo = atual + anterior
