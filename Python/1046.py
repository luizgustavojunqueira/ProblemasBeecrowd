inicio, fim = map(int, input().split())

if fim > inicio:
    duracao = fim - inicio
else:
    duracao = fim + 24 - inicio

print("O JOGO DUROU {} HORA(S)".format(duracao))