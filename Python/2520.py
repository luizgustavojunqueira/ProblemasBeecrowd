while True:
    try:

        n, m = map(int, input().split())

        mapa = []

        posx, posy, posAx, posAy = 0, 0, 0, 0

        for i in range(n):
            mapa.append(list(map(int, input().split())))
            if 2 in mapa[i]:
                posAy = mapa[i].index(2)
                posAx = i
            if 1 in mapa[i]:
                posy = mapa[i].index(1)
                posx = i

        tempo = 0

        while (posx != posAx or posy != posAy):

            if posx > posAx:
                posx -= 1
            elif posx < posAx:
                posx += 1
            elif posy > posAy:
                posy -= 1
            elif posy < posAy:
                posy += 1

            tempo += 1

        print(tempo)    

    except EOFError:
        break