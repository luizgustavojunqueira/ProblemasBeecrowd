n = int(input())

vogais = "aeiou"

for i in range(n):
    nome = input()
    nomeLower = nome.lower()

    facil = True

    for j in range(len(nomeLower) - 2):
        if (nomeLower[j] not in vogais and nomeLower[j+1] not in vogais and nomeLower[j+2] not in vogais):
            facil = False

    if facil:
        print(f"{nome} eh facil")
    else:
        print(f"{nome} nao eh facil")