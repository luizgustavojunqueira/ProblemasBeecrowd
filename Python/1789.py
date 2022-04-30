while True:
    try:
        numLesmas = int(input())
        velocidades = input().split()
        maisVeloz = 0
        for i in range(numLesmas):
            velocidades[i] = int(velocidades[i])
            if velocidades[i] > maisVeloz:
                maisVeloz = velocidades[i]

        if maisVeloz < 10:
            print(1)
        elif maisVeloz < 20:
            print(2)
        else:
            print(3)
        
    except EOFError:
        break