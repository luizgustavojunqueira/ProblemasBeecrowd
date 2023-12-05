while True:
    try:

        n = int(input())
                
        velocidades = []
        
        for i in range(n):
            t, d = map(int, input().split())
            velocidades.append(d/t)
            
        print(1)
            
        for i in range(n):
            recorde = False
            for j in range(i):
                if velocidades[j] < velocidades[i]:
                    recorde = True
                else:
                    recorde = False
                    break
                
            if recorde:
                print(i+1)
            
    except EOFError:
        break