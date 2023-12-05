while True:
    
    try:
        
        tabuleiro = []
        n, m = map(int, input().split())
        soma = 0
        
        for i in range(n):
            tabuleiro.append(list(map(int, input().split())))
            for j in range(m):
                if tabuleiro[i][j] == 1:
                    tabuleiro[i][j] = 9
            
        for i in range(n):
            for j in range(m):
                if tabuleiro[i][j] != 9:
                    if i > 0:
                        if tabuleiro[i-1][j] == 9:
                            soma += 1
                    if i < n - 1:
                        if tabuleiro[i+1][j] == 9:
                            soma += 1
                    if j > 0:
                        if tabuleiro[i][j-1] == 9:
                            soma += 1
                    if j < m - 1:
                        if tabuleiro[i][j+1] == 9:
                            soma += 1
                    
                    tabuleiro[i][j] = soma
                    soma = 0
        
        for i in range(n):
            for j in range(m):
                print(tabuleiro[i][j], end = "")
            print()

    except EOFError:
        break