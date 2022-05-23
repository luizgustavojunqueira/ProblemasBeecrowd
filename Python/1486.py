numPontos, numMedicoes, cPalitos = map(int, input().split())

while numPontos != 0 and numMedicoes != 0 and cPalitos != 0:
    
    qntPalitos = 0
    valLidos = [0 for v in range(numPontos)]

    for i in range(numMedicoes):
        valores = list(map(int, input().split()))
        
        for j in range(numPontos):
            if valores[j] == 1:
                valLidos[j] += 1
            else:
                valLidos[j] = 0
                
            if valLidos[j] == cPalitos:
                qntPalitos += 1
                
    print(qntPalitos)
    
    numPontos, numMedicoes, cPalitos = map(int, input().split())
