t = int(input())

def interseccao(cx, cy, raio, rx, ry, w, h):
    cDx = abs(cx - (rx + w / 2))
    cDy = abs(cy - (ry + h / 2))
    
    if cDx > ((w/2) + raio) or cDy > (h / 2 + raio):
        return False
    elif cDx <= (w/2) or cDy <= h/2:
        return True
    else:
        return (((cDx - w/2) ** 2) + ((cDy - h/2) ** 2)) <= (raio ** 2)
    
magia_raio = {"fire": {"1": 20, "2": 30, "3": 50}, "water": {"1": 10, "2": 25, "3": 40}, "earth": {"1": 25, "2": 55, "3": 70}, "air": {"1": 18, "2": 38, "3": 60}}

dano = {"fire": 200, "water": 300, "earth": 400, "air": 100}

for i in range(t):
    w, h, x0, y0 = map(int, input().split())
    linha2 = list(input().split())
    magia, n, cx, cy = linha2[0], linha2[1], int(linha2[2]), int(linha2[3])

    if interseccao(cx, cy, magia_raio[magia][n], x0, y0, w, h) == True:
        print(dano[magia])
    else:
        print(0)