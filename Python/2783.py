n, c, m = map(int, input().split())
carimbadas = list(map(int, input().split()))
compradas = list(map(int, input().split()))
carimbadasCompradas = []

qntFalta = c

for i in range(m):
    if compradas[i] in carimbadas and compradas[i] not in carimbadasCompradas:
        qntFalta -= 1
        carimbadasCompradas.append(compradas[i])

print(qntFalta) 