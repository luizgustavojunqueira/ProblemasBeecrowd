nc = int(input())

for i in range(nc):
    n, k = [int(i) for i in input().split()]
    circulo = [i+1 for i in range(n)]

    pos = ((k-1) % n)
    while len(circulo) > 1:
        circulo.pop(pos)

        pos += k - 1
        pos = (pos % len(circulo))

    print(f"Case {i+1}: {circulo[0]}")