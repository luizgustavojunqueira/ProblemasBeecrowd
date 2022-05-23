def ehPrimo(n):
    if n <= 3:
        return n > 1
    if not n % 2 or not n % 3:
        return False
    
    i = 5
    
    stop = int(n**0.5)
    
    while i <= stop:
        if not n%i or not n%(i+2):
            return False
        i += 6
    
    return True

while True:
    try:
        
        n = input()      
        primo = ehPrimo(int(n))
        super = False
        
        if primo:
            for i in range(len(n)):
                super = ehPrimo(int(n[i]))
                if not super:
                    break
            if super:
                print("Super")
            else:
                print("Primo")
        else:
            print("Nada")
        
    except EOFError:
        break