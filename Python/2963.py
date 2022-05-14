n = int(input())

votosCarlos = int(input())
maior = votosCarlos

for i in range(1, n):
    v = int(input())

    if v > maior:
        maior = v

if maior == votosCarlos:
    print("S")
else:
    print("N")