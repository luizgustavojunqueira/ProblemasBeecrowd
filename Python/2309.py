n = int(input())

adalberto, bernadete = 0, 0

valoresCartas = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]

for i in range(n):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    
    rodadasA, rodadasB = 0, 0
    
    if valoresCartas.index(a1) < valoresCartas.index(b1):
        rodadasB += 1
    else:
        rodadasA += 1
    
    if valoresCartas.index(a2) < valoresCartas.index(b2):
        rodadasB += 1
    else:
        rodadasA += 1
        
    if valoresCartas.index(a3) < valoresCartas.index(b3):
        rodadasB += 1
    else:
        rodadasA += 1
        
    if rodadasA >= rodadasB:
        adalberto += 1
    else:
        bernadete += 1
        
print(adalberto, bernadete)