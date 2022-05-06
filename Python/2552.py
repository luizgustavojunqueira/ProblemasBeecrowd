while True:
    
    try:
        
        tabuleiro = []
        n, m = map(int, input().split())
        
        res = []
        
        for i in range(n):
            tabuleiro.append(list(map(int, input().split())))
            res.append([])
            for j in range(m):
                res[i].append(0)

        print(res)
        
        for i in range(n):
            for j in range(m):
                if tabuleiro[i][j] == 1:
                    res[i][j] = 9
                else:
                    if i == 0:
                        if j == 0:
                            res[i][j] = tabuleiro[i][j+1] + tabuleiro[i+1][j]
                        elif j == m-1:
                            res[i][j] = tabuleiro[i][j-1] + tabuleiro[i+1][j]
                        else:
                            res[i][j] = tabuleiro[i][j+1] + tabuleiro[i][j-1] + tabuleiro[i+1][j]
                    elif i == n-1:                            
                        if j == 0:
                            res[i][j] = tabuleiro[i][j+1] + tabuleiro[i-1][j]
                        elif j == m-1:
                            res[i][j] = tabuleiro[i][j-1] + tabuleiro[i-1][j]
                        else:
                            res[i][j] = tabuleiro[i][j+1] + tabuleiro[i][j-1] + tabuleiro[i-1][j]
                    else:
                        if j == 0:
                            res[i][j] = tabuleiro[i][j+1] + tabuleiro[i+1][j] + tabuleiro[i-1][j]
                        elif j == m-1:
                            res[i][j] = tabuleiro[i][j-1] + tabuleiro[i+1][j] + tabuleiro[i-1][j]
                        else:
                            res[i][j] = tabuleiro[i][j+1] + tabuleiro[i][j-1] + tabuleiro[i+1][j] + tabuleiro[i-1][j] 
        
        for i in range(n):
            print(res[i])

    except EOFError:
        break