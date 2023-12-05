while True:
    try:
        
        vogais = input()
        
        totalVogais = 0
        
        frase = input()
        
        for i in range(len(frase)):
            if frase[i] in vogais:
                totalVogais += 1
                
        print(totalVogais)
        
    except EOFError:
        break