while True:
    try:

        m = int(input())

        valoresMoedas = []

        for i in range(m):
            valoresMoedas.append(int(input()))

        passoSomatoria = int(input())

        soma = 0

        for i in range(m-1, -1, -passoSomatoria):
            soma += valoresMoedas[i]

        numDivisores = 0

        for i in range(1, soma+1):
            if soma % i == 0:
                numDivisores += 1

        if numDivisores == 2:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")

    except:
        break