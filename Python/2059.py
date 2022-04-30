p, j1, j2, r, a = map(int, input().split())

res = j1 + j2

if res % 2 == 0:
    if p == 1:
        if r == 1:
            if a == 1:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
        else:
            print("Jogador 1 ganha!")
    else:
        if r == 1:
            if a == 1:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")      
elif res % 2 == 1:
    if p == 0:
        if r == 1:
            if a == 1:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
        else:
            print("Jogador 1 ganha!")
    else:
        if r == 1:
            if a == 1:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")      
