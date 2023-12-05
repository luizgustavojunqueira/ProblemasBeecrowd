def calcularTempo(numeros, tempos):
    t = len(numeros) - 1
    ordenado = False
    tempoTotal = 0

    while not ordenado:
        ordenado = True
        for i in range(t):
            if numeros[i] > numeros[i+1]:
                numeros[i], numeros[i + 1] = numeros[i+1], numeros[i]
                tempoTotal += tempos[i] + tempos[i+1]
                tempos[i], tempos[i+1] = tempos[i+1], tempos[i]
                ordenado = False
    
    return tempoTotal

while True:
    try:

        n = int(input())

        numeros = list(map(int, input().split()))
        tempos = list(map(int, input().split()))

        print(calcularTempo(numeros, tempos))

    except EOFError:
        break