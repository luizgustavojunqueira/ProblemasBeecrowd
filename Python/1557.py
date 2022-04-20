n = int(input())

while n > 0:

    m = []

    for i in range(n):
        m.append([])
        if i == 0:
            m[0].append(1)
        else:
            m[0].append(m[0][i-1] * 2 )  
        
    for i in range(1, n):
        m[i] = m[i-1][1:] + [m[i-1][n-1] * 2]

    qntDigitosMaior = len(str(m[n-1][n-1]))

    for i in range(n):
        linha = ''
        for j in range(n):
            stringVal = str(m[i][j])
            linha += (" " * (qntDigitosMaior-len(stringVal) + 1)) + stringVal
        print(linha[1:])
    print("")

    n = int(input())