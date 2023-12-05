n = int(input())

for i in range(n):
    frase = input()
    passo = int(input())
    
    fraseRes = ""
    
    for j in range(len(frase)):
        letraNova = (ord(frase[j]) - passo)
        if letraNova < 65:
            letraNova = 26 + letraNova
        
        fraseRes += chr(letraNova)
        
    print(fraseRes)