maiorPalavra = ""
maiorTamanho = 0

while True:
    s = input()
    
    if s == "0":
        break
    
    palavras = s.split()
    tamanhos = []
    
    for i in range(len(palavras)):
        tamanho = len(palavras[i])
        if tamanho >= maiorTamanho:
            maiorTamanho = tamanho
            maiorPalavra = palavras[i]
            
        tamanhos.append(str(tamanho))
        
    print("-".join(tamanhos))
    
print()
print(f"The biggest word: {maiorPalavra}")