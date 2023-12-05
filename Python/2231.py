n, m = map(int, input().split())

teste = 1

while n != 0 and m != 0:
    
    temperaturas = []
    medias = []
    
    for i in range(n):
        temperaturas.append(int(input()))
        
    for i in range(n - m + 1):
        media = int(sum(temperaturas[i: i+m]) / m)
        medias.append(media)
        
    maior = max(medias)
    menor = min(medias)
            
    print(f"Teste {teste}")
    print(f"{menor} {maior}")
    print()
    
    print(medias)
    
    n, m = map(int, input().split())
    teste += 1