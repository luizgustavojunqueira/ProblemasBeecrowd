l, a, p, r = map(int, input().split())

diagCaixa = (l ** 2 + a ** 2 + p ** 2) ** (1/2)

if diagCaixa <= 2*r:
    print("S")
else:
    print("N")