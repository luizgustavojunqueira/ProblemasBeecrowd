n, m = map(int, input().split())

matriz = []

for i in range(n):
    matriz.append(list(map(int, input().split())))

posMaisAEsquerda = []

for i in range(n): 

    ehLinhaDeZeros = True
    for j in range(m):
        if matriz[i][j] != 0:
            posMaisAEsquerda.append(j)
            ehLinhaDeZeros = False
            break
    
    if ehLinhaDeZeros:
        if len(posMaisAEsquerda) > 0:
            posMaisAEsquerda.append(posMaisAEsquerda[-1] + 1)
        else:
            posMaisAEsquerda.append(0)

ehEscada = True

for i in range(n-2):
    if posMaisAEsquerda[i] >= posMaisAEsquerda[i+1]:
        ehEscada = False
    
if ehEscada:
    print("S")
else:
    print("N")