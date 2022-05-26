t = int(input())

for i in range(t):
    n = int(input())

    nomes = [n for n in input().split()]
    frequencias = [n for n in input().split()]
    estudantesSemPresencaMinima = []

    for j in range(n):
        qntPresencas = 0
        qntAtestados = 0

        for c in frequencias[j]:
            if c == "P":
                qntPresencas += 1
            if c == "M":
                qntAtestados += 1

        qntAulas = len(frequencias[j]) - qntAtestados

        if (qntAulas * 3/4) > qntPresencas:
            estudantesSemPresencaMinima.append(nomes[j])
    
    print(" ".join(estudantesSemPresencaMinima))