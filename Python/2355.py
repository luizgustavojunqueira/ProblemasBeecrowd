import math

n = int(input())

while n > 0:
    qntAle = math.ceil(n*7/90)
    qntBr = math.floor(n/90)
    
    print(f"Brasil {qntBr} x Alemanha {qntAle}")
    
    n = int(input())