n = int(input())

while n > 0:

    m = []

    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(j+1)

    for i in range(1, n):
        m[i] = [m[i-1][0] + 1] + m[i-1][:n-1]
            
    for i in range(n):
        linha = ''
        for j in range(n):
            linha += " %3s" %m[i][j]
        print(linha[1:])
    print("")

    n = int(input())
