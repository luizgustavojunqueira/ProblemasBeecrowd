nAbas, nAcoes = map(int, input().split())

for i in range(nAcoes):
    acao = input()
    if acao == "fechou":
        nAbas += 1
    elif acao == "clicou":
        nAbas -= 1
    
print(nAbas)