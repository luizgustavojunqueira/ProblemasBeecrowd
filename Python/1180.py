n = int(input())
x = input().split()

for i in range(n):
    x[i] = int(x[i])

menor = x[0]
pos = 0

for i in range(n):
    if x[i] < menor:
        menor = x[i]
        pos = i

print(f"Menor valor: {x[pos]}")
print(f"Posicao: {pos}")