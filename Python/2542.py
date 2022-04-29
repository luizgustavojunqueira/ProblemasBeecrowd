while True:
    try:

        n = int(input())

        m, l = map(int, input().split())

        cartasM = [] 
        cartasL = []

        for i in range(m):
            cartasM.append(list(map(int, input().split())))

        for i in range(l):
            cartasL.append(list(map(int, input().split())))

        cm, cl = map(int, input().split())

        a = int(input())

        if cartasM[cm-1][a-1] > cartasL[cl-1][a-1]:
            print("Marcos")
        elif cartasM[cm-1][a-1] < cartasL[cl-1][a-1]:
            print("Leonardo")
        else:
            print("Empate")

    except EOFError:
        break