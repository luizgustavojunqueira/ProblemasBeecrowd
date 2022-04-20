n = int(input())

while n > 0:

    m = []

    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(1)
        
    for i in range(n-1):
        for j in range(i, n-i):
            for k in range(i, n-i):
                m[j][k] = i+1 
            
    for i in range(n):
        linha = ''
        for j in range(n):
            linha += " %3s" %m[i][j]
        print(linha[1:])
    print("")

    n = int(input())
