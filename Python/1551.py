n = int(input())

alf = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
    
    letrasDoAlf = []
    frase = input()
    
    for j in range(len(frase)):
        if frase[j] not in letrasDoAlf and frase[j] in alf:
            letrasDoAlf.append(frase[j])
            
    qntLetras = len(letrasDoAlf)
    if qntLetras == 26:
        print("frase completa")
    elif qntLetras >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")