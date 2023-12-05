n = int(input())
tabuleiro = []

for i in range(n):
    tabuleiro.append(int(input()))

if n > 1:
    res = [tabuleiro[0] + tabuleiro[1]]

    for i in range(1, n-1):
        res.append(tabuleiro[i] + tabuleiro[i+1] + tabuleiro[i-1])

    res.append(tabuleiro[n-2] + tabuleiro[n-1])

    for i in range(n):
        print(res[i])
else:
    print(tabuleiro[0])