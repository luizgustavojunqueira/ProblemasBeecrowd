n, m = map(int, input().split())

while n != 0 and m != 0:
    
    bilhetes = list(map(int, input().split()))
    
    bilhetesDuplicados = []
    
    for i in range(m):
        if bilhetes[i] not in bilhetesDuplicados and bilhetes[i] in bilhetes[i+1:]:
            bilhetesDuplicados.append(bilhetes[i])
            
    print(len(bilhetesDuplicados))
    
    n, m = map(int, input().split())