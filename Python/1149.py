entrada = input().split()

a = int(entrada[0])

n = 0

for i in range(1, len(entrada)):
    if int(entrada[i]) > n:
        n = int(entrada[i])

soma = 0

for i in range(0, n):
    soma += a+i

print(soma)