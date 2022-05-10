t = int(input())
saida = []

for i in range(t):
    w, h, x0, y0 = map(int, input().split())
    linha2 = list(input().split())
    magia, n, cx, cy = linha2[0], int(linha2[1]), int(linha2[2]), int(linha2[3])

    dano = 0
    deuDano = False

    if n == 1:
        if cx - 20 <= x0 + h <= cx + 20 and cy - 20 <= y0 + h <= cy + 20:
            deuDano = True
    elif n == 2:
        if cx - 30 <= x0 + h <= cx + 30 and cy - 30 <= y0 + h <= cy + 30:
            deuDano = True
    elif n == 3:
        if cx - 50 <= x0 + h <= cx + 50 and cy - 50 <= y0 + h <= cy + 50:
            deuDano = True
    
    if deuDano:
        if magia == "fire":
            dano = 200
        elif magia == "water":
            dano = 300
        elif magia == "earth":
            dano = 400
        elif magia == "air":
            dano = 100

    saida.append(dano)

for i in range(t):
    print(saida[i])