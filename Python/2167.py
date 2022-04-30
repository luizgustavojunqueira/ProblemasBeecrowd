n = int(input())

medidas = list(map(int, input().split()))
indice = 0

for i in range(1, n):
    if medidas[i] < medidas[i-1]:
        indice = i+1
        break

print(indice)