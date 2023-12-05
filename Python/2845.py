n = int(input())

identifiers = list(map(int, input().split()))

maior = 0

for i in range(n):
    if identifiers[i] > maior:
        maior = identifiers[i]

print(maior + 1)