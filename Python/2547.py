while True:
    try:
    
        n, amin, amax = map(int, input().split())
        
        numPermitidos = 0
        
        for i in range(n):
            altura = int(input())
            
            if amin <= altura <= amax:
                numPermitidos += 1
                
        print(numPermitidos)

    except EOFError:
        break