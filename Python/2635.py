n = int(input())

palavras = []

for i in range(n):
    palavras.append(input())

q = int(input())

for i in range(q):
    pesquisa = input()
    tamanhoPesquisa = len(pesquisa)

    qntSugestoes = 0
    tamanhoMaiorSugestao = 0
    for j in range(n):
        if palavras[j][:tamanhoPesquisa] == pesquisa:
            qntSugestoes += 1
            tamanhoPalavra = len(palavras[j])

            if tamanhoPalavra > tamanhoMaiorSugestao:
                tamanhoMaiorSugestao = tamanhoPalavra

    if qntSugestoes:
        print(qntSugestoes, tamanhoMaiorSugestao)
    else:
        print(-1)