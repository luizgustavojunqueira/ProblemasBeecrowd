n = int(input())

while n != 0:
    
    relacoes = input().split()

    for i in range(n):
        relacoes[i] = relacoes[i].split(',')
        relacoes[i] = [int(relacoes[i][0].split("(")[1]), int(relacoes[i][1].split(")")[0])]

    convidados = [1]


    for i in range(n):
        

    print(len(convidados))

    n = int(input())