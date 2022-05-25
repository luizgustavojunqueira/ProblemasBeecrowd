n, m = [int(i) for i in input().split()]
posicoes = [int(i) for i in input().split()]
posicoes.append(42195)

possivel = True

for i in range(n):
    if (posicoes[i+1] - posicoes[i]) > m:
        possivel = False
        break

if possivel:
    print("S")
else:
    print("N")