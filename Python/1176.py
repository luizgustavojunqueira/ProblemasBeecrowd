t = int(input())

fib = []

anterior = 0
atual = 0
proximo = 1

for i in range(61):
    fib.append(atual)
    anterior = atual
    atual = proximo
    proximo = atual + anterior

for i in range(t):
    x = int(input())
    print(f"Fib({x}) = {fib[x]}")