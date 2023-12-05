n = int(input())
m = int(input())

compradas = []

for i in range(m):
    x = int(input())

    if not (x in compradas):
        compradas.append(x)

print(n - len(compradas))